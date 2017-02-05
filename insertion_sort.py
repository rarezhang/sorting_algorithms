"""
insertion sort
"""


def insertion_sort(L):
    """
    builds the final sorted list one item at a time
    :param L: python list
    :return:
    >>> insertion_sort([4,3,2,5])
    [2, 3, 4, 5]
    >>> insertion_sort([])
    []
    >>> insertion_sort([1])
    [1]
    """
    assert isinstance(L, list)
    length = len(L)
    # outer loop: runs over all the elements except the first one (1st element already sorted)
    for i in range(1, length):  # start with the 2nd element
        current_value = L[i]
        j = i-1
        # inner loop: moves element L[i] to its correct place so that after the loop, the first i+2 elements are sorted.
        while j>=0 and L[j]>current_value:  # find appropriate position for insertion
            L[j+1] = L[j]
            j -= 1
        L[j+1] = current_value
    return L

