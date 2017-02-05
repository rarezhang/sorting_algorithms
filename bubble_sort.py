"""
bubble sort
"""

def bubble_sort(L):
    """
    repeatedly steps through the list to be sorted,
    compares each pair of adjacent items and swaps them
    if they are in the wrong order
    :param L: python list
    :return:
    >>> bubble_sort([4,3,2,5])
    [2, 3, 4, 5]
    >>> bubble_sort([])
    []
    >>> bubble_sort([1])
    [1]
    """
    assert isinstance(L, list)
    length = len(L)
    for i in range(length-1):
        for j in range(length-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]  # swap
    return L
