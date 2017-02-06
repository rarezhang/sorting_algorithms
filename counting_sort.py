"""
counting sort
"""


def counting_sort(L):
    """
    an integer sorting algorithm
    :param L: python list
    :return:
    >>> counting_sort([4,3,2,5])
    [2, 3, 4, 5]
    >>> counting_sort([])
    []
    >>> counting_sort([1])
    [1]
    """
    assert isinstance(L, list)
    if len(L) < 2:
        return L

    max_value = max(L)
    counter = [0] * (max_value + 1)  # Since the values range from 0 to k, create k+1 buckets

    # To fill the buckets, iterate through the input list and
    #  each time a value appears, increment the counter in its
    #  bucket.
    for i in L:
        counter[i] += 1

    #  fill the input list with the compressed data in the buckets.
    #  Each bucket's key represents a value in the array.
    #  So for each bucket, from smallest key to largest,
    #  add the index of the bucket to the input array and
    #  decrease the counter in said bucket by one; until the
    #  counter is zero.
    L_index = 0
    for j in range(max_value+1):
        while counter[j] > 0:
            L[L_index] = j
            L_index += 1
            counter[j] -= 1
    return L

