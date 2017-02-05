"""
Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1.
https://youtu.be/qzXAVXddcPU
"""


def shell_sort(L):
    """
    improves on the insertion sort by breaking the original list into a number of smaller sub-lists,
    each of which is sorted using an insertion sort
    :param L: python list
    :return:
    >>> shell_sort([4,3,2,5])
    [2, 3, 4, 5]
    >>> shell_sort([])
    []
    >>> shell_sort([1])
    [1]
    """
    assert isinstance(L, list)

    length = len(L)
    gap = length // 2
    while gap > 0:
        # ------- insertion sort ---------------
        for i in range(gap, length):
            current_value = L[i]
            j = i
            while j >= gap and L[j-gap] > current_value:
                L[j] = L[j-gap]
                j -= gap
            L[j] = current_value
        # ------- insertion sort ---------------
        gap //= 2
    return L
