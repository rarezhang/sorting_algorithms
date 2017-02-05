"""
selection sort
"""

def selection_sort(L):
    """
    in-place comparison sort
    :param L: python list
    :return:
    >>> selection_sort([4,3,2,5])
    [2, 3, 4, 5]
    >>> selection_sort([])
    []
    >>> selection_sort([1])
    [1]
    """
    assert isinstance(L, list)
    length = len(L)
    for i in range(length):
        i_small = i
        for j in range(i, length):
            if L[i_small] > L[j]:  # find the index of the (current) smallest item
                i_small = j
        L[i], L[i_small] = L[i_small], L[i]  # put the (current) smallest item at the front end
    return L

