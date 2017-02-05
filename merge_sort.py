"""
merge sort
"""


def _merge(L1, L2, L):
    """
    merge two sorted lists into properly sized list
    :param L1:
    :param L2:
    :param L:
    :return:
    """
    i = j = 0
    while i+j < len(L):
        if j == len(L2) or (i < len(L1) and L1[i] < L2[j]):
            # j==len(L2) -> L2 end
            # i < len(L1) and L1[i] < L2[j] -> L1 not end, L1 has smaller item
            L[i+j] = L1[i]  # copy ith element of L1 as next item of L
            i += 1
        else:
            L[i+j] = L2[j]  # copy jth element of L2 as next item of L
            j += 1
    return L


def merge_sort(L):
    """
    comparison-based sorting algorithm.
    :param L: python list
    :return:
    >>> merge_sort([4,3,2,5])
    [2, 3, 4, 5]
    >>> merge_sort([])
    []
    >>> merge_sort([1])
    [1]
    """
    assert isinstance(L, list)
    length = len(L)
    if length < 2:  # already sorted
        return L
    else:
        mid = length // 2
        L1 = L[:mid]  # copy of first half
        L2 = L[mid:]  # copy of second half
        # conquer with recursion
        merge_sort(L1)
        merge_sort(L2)
        # merge results
        return _merge(L1, L2, L)  # merge sorted halves back into L