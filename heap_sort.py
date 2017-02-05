"""
heap sort
"""


def heap_sort(L):
    """
    Creating a Heap of the unsorted list. Then a sorted array is created by repeatedly removing the largest/smallest
    element from the heap, and inserting it into the array.
    :param L: python list
    :return:
    >>> heap_sort([4,3,2,5])
    [2, 3, 4, 5]
    >>> heap_sort([])
    []
    >>> heap_sort([1])
    [1]
    """
    assert isinstance(L, list)
    H = Heap(L)
    for i in L:
        H.push(i)
    return [H.pop() for _ in range(len(L))]



class Heap:
    """
    simple heap
    """


    def __init__(self, data):
        """
        create a new empty heap
        """
        self._data = []

    def push(self, value):
        """
        add a value to the heap
        :param value:
        :return:
        """
        self._data.append(value)
        # upheap: put smallest item at the root
        self._upheap(len(self._data)-1)  # upheap newly added item, position = len(_data)-1

    def pop(self):
        """
        return minimum value
        :return:
        """
        if len(self._data)==0:
            return
        self._swap(0, len(self._data)-1)  # put minimum item at the end
        value = self._data.pop()  # remove the mimimum item from the queue
        self._downheap(0)
        return value

    # ----------- non-public method -------------------------------
    def _swap(self, i, j):
        """
        swap the elements at indices i and j of array
        :param i:
        :param j:
        :return:
        """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        """
        up-ward swapping process; up-heap bubbling
        use recursion to implement the repetition
        :param j:
        :return:
        """
        parent = self._parent(j)  # get the index of parent
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)  # recursion at position of parent

    def _downheap(self, j):
        """
        down-ward swapping process; down-heap bubbling
        use recursion to implement the repetition
        :param j:
        :return:
        """
        if self._has_left(j):
            left = self._left(j)  # index of left child
            small_child = left  # although right may be smaller
            if self._has_right(j):
                right = self._right(j)  # index of right child
                if self._data[right] < self._data[left]:
                    small_child = right
            # swap: smaller value bubble up
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    # ------------ helper methods ---------------------------------------
    # If p is the root of T, then f ( p ) = 0.
    # If p is the left child of position q, then f ( p ) = 2 f ( q )+ 1.
    # If p is the right child of position q, then f ( p ) = 2 f ( q )+ 2.
    def _parent(self, j):
        """
        return the index of parent
        :param j:
        :return:
        """
        return (j-1)//2

    def _left(self, j):
        """
        return the index of left child
        :param j:
        :return:
        """
        return 2*j+1

    def _right(self, j):
        """
        return the index of right child
        :param j:
        :return:
        """
        return 2*j+2

    def _has_left(self, j):
        """
        if there is left child, index beyond end of list?
        :param j:
        :return:
        """
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        """
        if there is right child, index beyond end of list?
        :param j:
        :return:
        """
        return self._right(j) < len(self._data)


###################### built-in heapq #################
import heapq


def heap_sort_heapq(L):
    """
    use python built-in heapq
    :param L:
    :return:
    >>> heap_sort_heapq([4,3,2,5])
    [2, 3, 4, 5]
    >>> heap_sort_heapq([])
    []
    >>> heap_sort_heapq([1])
    [1]
    """
    H = []  # help list
    for value in L:
        heapq.heappush(H, value)
    return [heapq.heappop(H) for _ in range(len(L))]