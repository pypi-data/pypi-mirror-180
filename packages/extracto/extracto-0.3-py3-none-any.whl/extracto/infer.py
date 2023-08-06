from .selectors import _candidate_selectors, _candidate_repeating_selectors

import itertools
import time
from .equals import _node_in, _height_of
from .extract import extract_rows
from .cache import _make_cached_tree_css

def _no_banned_nodes(tree_css_func, selector, reject):
    if not reject:
        return True

    nodes = tree_css_func(selector)
    for node in reject:
        if _node_in(node, nodes):
            return False

    return True

def infer_column(tree_css_func, tree, keep, reject=[], cache={}):
    """In the given tree, propose some candidate selectors that would find elements
       that have the values in "keep". (Some massaging may be needed, eg, stripping,
       reading an attribute.)

       Don't propose a selector if it would select a node in reject."""

    sets = []

    start_time = time.time()
    for needle in keep:
        choices = []

        needle_nodes = []
        for node in tree.root.traverse():
            for i, (k, v) in enumerate(node.attrs.items()):
                if k != 'class' and k != 'id' and k != 'data-preorder-index':
                    if v == needle:
                        choices.append((node, k, needle))
            # To avoid wasting a ton of resource, only check nodes that have
            # 0 or 1 kids, and 
            if not node.child or not node.child.next:
                t = node.text().strip()
                if t == needle and (not reject or not _node_in(node, reject)):
                    choices.append((node, None, needle))

        if not choices:
            print('infer_column failed after ' + str(time.time() - start_time))
            return []
        sets.append(choices)

    print('sets len: {} took: {}'.format([len(q) for q in sets], time.time() - start_time))
    # Create all the permutations of the sets
    permutations = list(itertools.product(*sets))

    # Try to find list of candidate selectors that find the nodes

    candidates = []
    total_time = 0
    for i, permutation in enumerate(permutations):
        #print('{}: {}'.format(i, permutation))
        t = time.time()
        selectors = list(set.intersection(*[set(_candidate_selectors(tree, node, cache=cache)) for (node, attribute, needle) in list(permutation)]))
        total_time += time.time() - t
        #print('intersection took {}'.format(time.time()-t))

        # Only accept if the selector doesn't pick any of the rejected nodes.
        selectors = [selector for selector in selectors if not reject or _no_banned_nodes(tree_css_func, selector, reject)]

        if selectors:
            # TODO: confirm this is true :)
            # this sort is just useful for debugging; doesn't affect
            # correctness, as we re-sort later after merging things
            #selectors.sort(key=lambda x: (len(x), x))
            candidates.append((permutation, selectors))
    print('intersection took {}'.format(total_time))

    print(len(candidates))

    return candidates

def _all_at_same_height(nodes):
    if not nodes:
        return False

    height = _height_of(nodes[0])

    for node in nodes:
        if _height_of(node) != height:
            return False

    return True


def _can_extract_examples(cached_tree_css, row_examples, candidate_repeating_selector, ok_attribute_selectors):
    """Confirm that the output of infer can produce the examples in row_examples.

This is necessary because we do a naive (but cheap!) search for selectors that _might_
be correct; so we need to do a second pass to confirm they're correct.
"""
    optional_attrs = []
    for i in range(len(row_examples[0])):
        is_optional = False
        for j in row_examples:
            if j[i] == None:
                is_optional = True

        optional_attrs.append(is_optional)

    #print(candidate_repeating_selector + ': ' + str(ok_attribute_selectors))

    attrs = []
    for i, attribute_selector in enumerate(ok_attribute_selectors):
        attrs.append({
            'selector': attribute_selector[0][0],
            'optional': optional_attrs[i],
            'conversions': ['@' + attribute_selector[0][1]] if attribute_selector[0][1] else []
        })

    extract_params = {
        'selector': candidate_repeating_selector,
        'columns': attrs
    }

    #print(attrs)
    extracted = extract_rows(
        cached_tree_css,
        extract_params
    )

    ok = True
    for row in row_examples:
        if not row in extracted:
            ok = False
            break

    if ok:
        return extract_params

    return False

def _ban_duplicate_selectors(candidate_selector_sets):
    """Remove selectors that are present in multiple attributes; it's unlikely something
       is the correct selector for, say, name and price simultaneously."""
    rv = []
    selector_count = {}
    for candidate_selector_set in candidate_selector_sets:
        for y in candidate_selector_set:
            selector_count[y] = selector_count.get(y, 0) + 1

    banned_selector = {}
    for i, (k, v) in enumerate(selector_count.items()):
        if v > 1:
            banned_selector[k] = True

    for candidate_selector_set in candidate_selector_sets:
        rv.append({x for x in candidate_selector_set if not x in banned_selector})

    print('! banned_selector size is {}, old was {}, new is {}'.format(len(banned_selector), [len(x) for x in candidate_selector_sets], [len(x) for x in rv]))

    return rv


def infer_rows(tree, row_examples):
    cache = {}
    # NB: you must have called annotate_preorder on the tree; we use the preorder indexes
    #     to cache css selector evaluations, and eventually, to prune the search space
    if not row_examples:
        raise Exception('need to provide at least one row example')

    cached_tree_css = _make_cached_tree_css(tree)

    for row_example in row_examples:
        if len(row_example) != len(row_examples[0]):
            raise Exception('all row examples should be the same length (' + str(len(row_examples[0])) + '): ' + str(row_example))

        all_empty = True
        for attr in row_example:
            if attr:
                all_empty = False

        if all_empty:
            raise Exception('at least one attribute in the row must be defined: ' + str(row_example))

    print(row_examples)

    # If an attribute is a "singleton", it means it's unique across all the examples
    # and should be computed relative to the HTML root, not relative to a repeating
    # selector. (This can cause false positives! The user will have to ensure they
    # add examples that are _not_ unique.)
    singleton_attributes = []
    optional_attributes = []
    attribute_conversion_choices = []
    max_distinct_attribute_values = 0

    # Pivot the row examples so instead of logical rows, we have all the birth years,
    # all the first names, etc
    attribute_examples = []
    for i in range(len(row_examples[0])):
        is_singleton = True
        all_empty = True
        some_empty = False
        attribute_examples.append([row_example[i] for row_example in row_examples])

        attribute_values = {}

        for x in attribute_examples[-1]:
            attribute_values[x] = True
            if x != attribute_examples[-1][0]:
                is_singleton = False

            if x:
                all_empty = False
            else:
                some_empty = True

        distinct_attribute_values = len([x for x in attribute_values.keys() if not x is None])

        if distinct_attribute_values > max_distinct_attribute_values:
            max_distinct_attribute_values = distinct_attribute_values
        singleton_attributes.append(is_singleton)
        optional_attributes.append(some_empty)

        if all_empty:
            raise Exception('you must provide at least one non-null example for attribute ' + str(i))

    print(attribute_examples)

    attribute_selectors = []

    t = time.time()
    for i in range(len(attribute_examples)):

        reject = []
        #for j in range(len(attribute_examples)):
        #   if i == j:
        #       continue

        #   for needle in attribute_examples[j]:
        #       if not needle in attribute_examples[i]:
        #           reject.append(needle)


        # TODO: do we need to 2 passes of infer_column? Once to find the nodes that
        #       are candidates, and a second time to exclude those nodes from the other
        #       attributes.
        qq = time.time()

        selectors = infer_column(cached_tree_css, tree, [x for x in attribute_examples[i] if x], reject, cache=cache)
        print('! infer_column[{}] took {} from examples {} (reject={})'.format(i, time.time() - qq, attribute_examples[i], reject))
        attribute_conversion_choices.append(list({attr[1] for q in selectors for attr in q[0]}))

        if not selectors:
            raise Exception('unable to infer candidates for attribute ' + str(i) + ': ' + str(attribute_examples[i]))

        # TODO: consider deleting this; it's convenient during development to see interim things
        #       sorted by "goodness", but it'll get shaken out later, too
        for opts in selectors:
            opts[1].sort(key=lambda x: (len(x), x))

        # Ensure that singleton attributes always have 'html' style selectors
        if singleton_attributes[i]:
            for opts in selectors:
                for i in range(len(opts[1])):
                    if not opts[1][i].startswith('html '):
                        opts[1][i] = 'html ' + opts[1][i]

        attribute_selectors.append(selectors)

    print('! infer_column(s) took {}'.format(time.time()-t))
    t = time.time()

    candidate_selector_sets = []
    attribute_nodes = []
    for i, attribute_selector in enumerate(attribute_selectors):
        candidate_selector_sets.append({y for x in attribute_selector for y in x[1]})
        nodes_i = {}
        for (node, attribute, label) in [y for x in attribute_selector for y in x[0]]:
            nodes_i[node.attrs['data-preorder-index']] = node

        attribute_nodes.append(nodes_i.values())


    print('! intersecting took {}'.format(time.time() - t))
    #print('candidate_selector_sets[0] = {}'.format(candidate_selector_sets[0]))

    candidate_selector_sets = _ban_duplicate_selectors(candidate_selector_sets)

    t = time.time()
    candidate_repeating_selectors = _candidate_repeating_selectors(tree, singleton_attributes, attribute_nodes, cache=cache)

    print("! producing {} candidate_repeating_selectors took {}".format(len(candidate_repeating_selectors), time.time() - t))

    t = time.time()
    #print(candidate_repeating_selectors)

    ok_extract_params = []

    iterations_required = 0

    css_cache = {}
    opt = 0

    # TODO: future optimization
    # Test the attributes in order of the one with the _fewest_ candidate selectors first.
    # e.g. for relish, test price (3 selectors), then sale price (80), then title (671 !)
    #
    # This brings a _big_ speedup
    shortest_to_longest = []
    for i in range(len(candidate_selector_sets)):
        shortest_to_longest.append(i)

    shortest_to_longest.sort(key=lambda x: len(candidate_selector_sets[x]))
    print([len(x) for x in candidate_selector_sets])
    print('### shortest_to_longest={}'.format(shortest_to_longest))

    for candidate_repeating_selector in candidate_repeating_selectors:
        iterations_required += 1

        repeating_elements = cached_tree_css(candidate_repeating_selector)
        #print(candidate_repeating_selector + ': ' + str(len(repeating_elements)))

        # TODO: threshold should be chosen based on max(count(distinct value)) for an attribute
        #       attribute
        if len(repeating_elements) < max_distinct_attribute_values:
            continue

        if not _all_at_same_height(repeating_elements):
            continue
        #print('_all_at_same_height took {}'.format(time.time() - t))

        #print(' ok: ' + candidate_repeating_selector)

        all_attrs_ok = True
        ok_attribute_selectors = {}

        for orig_i in range(len(attribute_examples)):
            i = shortest_to_longest[orig_i]
            keepers = []
            for attribute_conversion in attribute_conversion_choices[i]:
                #print('! testing selectors for {} conversion={}'.format(attribute_examples[i], attribute_conversion))

                for attribute_selector in candidate_selector_sets[i]:
                    needed = {}
                    for example in [k for k in attribute_examples[i] if k]:
                        needed[example] = True

                    # If it's a singleton attribute, we should compute relative
                    # to the tree root.
                    search_roots = repeating_elements

                    if singleton_attributes[i]:
                        search_roots = [tree.root]

                    #print("search_roots is {}: testing {}".format(len(search_roots), attribute_selector))
                    for parent in search_roots:
                        el_id = parent.attrs['data-preorder-index']

                        # NB: this could be rewritten to use cached_tree_css,
                        #     but this is a tight loop and the function invocation
                        #     actually adds a lot of overhead :(
                        css_cache_key = el_id + '!' + attribute_selector
                        nodes = css_cache.get(css_cache_key)

                        if nodes is None:
                            nodes = parent.css(attribute_selector)

                            #if len(nodes) == 0:
                            #    print('css miss {}'.format(attribute_selector))
                            css_cache[css_cache_key] = nodes

                        if nodes:
                            if attribute_conversion == None:
                                needed.pop(nodes[0].text().strip(), 'ignore')
                            else:
                                needed.pop(nodes[0].attrs.get(attribute_conversion, ''), 'ignore')


                        if len(needed) == 0:
                            break

                    if len(needed) == 0:
                        keepers.append((attribute_selector, attribute_conversion))
                    #print('...took {}'.format(time.time()-t))

            if keepers:
                #print('found {} keepers of {}'.format(len(keepers), len(candidate_selector_sets[i])))
                # prefer shorter selectors, all else being equal
                keepers.sort(key=lambda x: (len(x[0]), x))
                #keepers = keepers[0:5]
                ok_attribute_selectors[i] = keepers
            else:
                break

        #print(ok_attribute_selectors)
        if len(ok_attribute_selectors) == len(attribute_examples):
            # Confirm we can extract the examples before accepting this selector, eg
            # we might have just found all the individual elements, but not as cohesive
            # rows
            #t = time.time()

            extract_params = _can_extract_examples(cached_tree_css, row_examples, candidate_repeating_selector, [ok_attribute_selectors[i] for i in range(len(ok_attribute_selectors))])
            #print('_can_extract_examples took {}'.format(time.time() - t))

            if not extract_params:
                continue

            ok_extract_params.append((candidate_repeating_selector, extract_params))
            break


    ok_extract_params.sort(key=lambda x: len(x[0]))
    print("performed {} searches in {}".format(iterations_required, time.time() - t))
    #print(ok_extract_params[0:5])
    #print(candidate_repeating_selectors)
    print('possible solutions: ' + str(len(ok_extract_params)) + ' of ' + str(len(candidate_repeating_selectors)))

    if ok_extract_params:
        return ok_extract_params[0][1]

    return None

