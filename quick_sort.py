"""
quick sort
"""


def quick_sort(L, low=0, high=None):
    """
    quick sort without additional memory
    comparison-based sorting algorithm.
    :param L: python list
    :return:
    >>> quick_sort([4,3,2,5])
    [2, 3, 4, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([1])
    [1]
    """
    assert isinstance(L, list)
    if high is None:
        high = len(L) - 1
    if high < low:  # no need to sort
        return L
    pivot = _partition(L, low, high)
    quick_sort(L, low, pivot-1)
    quick_sort(L, pivot+1, high)
    return L


def _partition(L, low, high):
    """

    :param L:
    :param low:
    :param high:
    :return:
    """
    pivot = low
    for i in range(low+1, high+1):
        if L[i] <= L[low]:
            pivot += 1
            L[i], L[pivot] = L[pivot], L[i]
    L[pivot], L[low] = L[low], L[pivot]
    return pivot


# ------------ with additional memory (easy to read) ------------
def quick_sort_memory(L):
    """
    with additional memory (easy to read)
    :param L: python list
    :return:
    >>> quick_sort_memory([4,3,2,5])
    [2, 3, 4, 5]
    """
    assert isinstance(L, list)
    lesser, equal, greater = [], [], []
    length = len(L)
    if length < 2:  # no need to sort
        return L
    else:
        pivot = L[0]
        for x in L:
            if x < pivot: lesser.append(x)
            elif x > pivot: greater.append(x)
            else: equal.append(x)
        return quick_sort_memory(lesser) + quick_sort_memory(equal) + quick_sort_memory(greater)