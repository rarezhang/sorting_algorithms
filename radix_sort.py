"""
radix sort
radix: the base of a system of numeration
"""


def radix_sort(L, radix=10):
    """
    non-comparative integer sorting algorithm
    :param L: python list
    :param radix: base
    :return:
    >>> radix_sort([4,33,21,56])
    [4, 21, 33, 56]
    >>> radix_sort([])
    []
    >>> radix_sort([1])
    [1]
    """
    assert isinstance(L, list)
    if len(L) < 2:
        return L

    max_length = False
    placement = 1

    while not max_length:  # run one more loop to get max_length=True
        max_length = True
        # declare and initialize buckets
        buckets = [[] for _ in range(radix)]  # how many buckets (depends on radix)

        for i in L:
            current_digit = i // placement
            buckets[current_digit % radix].append(i)
            if max_length and current_digit > 0:
                max_length = False
        # put sorted buckets elements back into L
        L = sum(buckets, [])
        # move to next digit
        placement *= radix
    return L

