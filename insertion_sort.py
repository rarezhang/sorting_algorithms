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
    for i in range(1, length):  # start with the 2nd element
        current_value = L[i]
        position = i
        while position>0 and L[position-1]>current_value: # find appropriate position for insertion
            L[position] = L[position-1]
            position -= 1
        L[position] = current_value
    return L

