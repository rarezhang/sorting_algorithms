# Sorting algorithms implemented in python


## bubble sort
- repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order  
    + Data structure: Array  
    + Worst-case performance: O(n**2)  
    + Best-case performance: O(n)  
    + Average performance: O(n**2)  
    + Worst-case space complexity: O(1)  
    
    
## selection sort
- an in-place comparison sort, divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the sublist of items remaining to be sorted that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right  
    + Data structure: Array  
    + Worst-case performance: O(n**2)  
    + Best-case performance: O(n**2)  
    + Average performance: O(n**2)  
    + Worst-case space complexity: О(n) total, O(1)  
    
    
## insertion sort 
- builds the final sorted array (or list) one item at a time. Maintains a sorted sublist in the lower positions of the list. Each new item is then "inserted" back into the previous sublist such that the sorted sublist is one item larger  
    + Data structure: Array  
    + Worst-case performance: O(n**2)  
    + Best-case performance: O(n)  
    + Average performance: O(n**2)  
    + Worst-case space complexity: О(n) total, O(1)  
    
    
## shell sort  
- an in-place comparison sort. Starts by sorting pairs of elements far apart from each other, then progressively reducing the gap between elements to be compared  
-  improves on the insertion sort by breaking the original list into a number of smaller sublists, each of which is sorted using an insertion sort  
    + Data structure: Array  
    + Worst-case performance: O(n*(log(n)*2))  
    + Best-case performance: O(n*lon(n))  
    + Average performance: depends on gap sequence  
    + Worst-case space complexity: О(n) total, O(1)  
    
    
## merge sort  
- comparison-based sorting algorithm. Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted). Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.
    + Data structure: Array  
    + Worst-case performance: O(n*lon(n))  
    + Best-case performance: O(n*lon(n))  
    + Average performance: O(n*lon(n))  
    + Worst-case space complexity: О(n) total, O(n)  
    
    
## quick sort  
- comparison-based sorting algorithm. First selects a value, which is called the pivot value. (many different ways to choose the pivot value, simply use the first item in the list) The role of the pivot value is to assist with splitting the list. The actual position where the pivot value belongs in the final sorted list, commonly called the split point, will be used to divide the list for subsequent calls to the quick sort (divide and conquer)  
    + Data structure: Array  
    + Worst-case performance: O(n**2)  
    + Best-case performance: O(n*lon(n)) (simple partition) or O(n) (three-way partition and equal keys)
    + Average performance: O(n*lon(n))  
    + Worst-case space complexity: О(n)  
    
    
## heap sort
- comparison-based sorting algorithm. Creating a Heap of the unsorted list. Then a sorted array is created by repeatedly removing the largest/smallest element from the heap, and inserting it into the array. The heap is reconstructed after each removal.
    + Data structure: Array  
    + Worst-case performance: O(n*lon(n))  
    + Best-case performance: O(n*lon(n))  
    + Average performance: O(n*lon(n))  
    + Worst-case space complexity: О(1)  
    
    
## bucket sort 
- a distribution sort. works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm.  
    + Data structure: Array  
    + Worst-case performance: O(n**2)  
    + Best-case performance: O(n+k)  
    + Average performance: O(n+k)  
    + Worst-case space complexity: О(n*k)  
    
    
## counting sort
- an integer sorting algorithm. works by counting the number of objects having distinct key values (kind of hashing). Then doing some arithmetic to calculate the position of each object in the output sequence.  
- For problem instances in which the maximum key value is significantly smaller than the number of items, counting sort can be highly space-efficient, as the only storage it uses other than its input and output arrays is the Count array which uses space O(k). 
    
    
## radix sort
- non-comparative integer sorting algorithm.   
    + Data structure: Array  
    + Worst-case performance: O((n+b) * logb(k))  
    + Average performance: O(d*(n+b)) time where b is the base for representing numbers
    + Worst-case space complexity: О(w+N)  

  
Note:
- Counting sort: buckets hold only a single value  
- Bucket sort: buckets hold a range of values  
- Radix sort: buckets hold values based on digits within their values  