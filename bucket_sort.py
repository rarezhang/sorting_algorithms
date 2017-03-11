"""
bucket sort
consider a sequence S of n entries whose keys are integers in the range [ 0 , N − 1 ], it is possible to sort S in O ( n + N ) time. 
because of the restrictive assumption
about the format of the elements, we can avoid using comparisons
not based on comparisons, but on using keys as indices into a bucket array B that has cells indexed from 0 to N − 1
bucket-sort is efﬁcient when the range N of values for the keys is small compared to the sequence size n, say N = O ( n ) or N = O ( nlogn ) 
"""

DEFAULT = 5


def bucket_sort(L, bucket_size=DEFAULT):
    """
    distributing the elements of an array into a number of buckets.
    Each bucket is then either using a different sorting algorithm,
    or by recursively applying the bucket sorting algorithm.
    :param L: python list
    :return:
    >>> bucket_sort([4,3,2,5])
    [2, 3, 4, 5]
    >>> bucket_sort([])
    []
    >>> bucket_sort([1])
    [1]
    """
    assert isinstance(L, list)
    length = len(L)
    if length < 2:  # no need to sort
        return L

    # determine minimum and maximum values
    max_value = max(L)  # O(n)
    # max_value = L[0]
    # for i in L:
    #     if i > max_value: max_value = i

    # initialize buckets
    bucket_count = (max_value // bucket_size) + 1
    buckets = [[] for _ in range(bucket_count)]

    # distribute values into buckets
    for i in L:
        buckets[i//bucket_size].append(i)
    # sort each bucket, place back into L
    for j in range(bucket_count):
        buckets[j].sort()  # any sort algorithm
    return [i for bucket in buckets for i in bucket]
    # return sum(buckets, [])  # [[], [], ...] -> []
