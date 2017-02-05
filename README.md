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
    
    
# merge sort  
- comparison-based sorting algorithm. Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted). Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.
    + Data structure: Array  
    + Worst-case performance: O(n*lon(n))  
    + Best-case performance: O(n*lon(n))  
    + Average performance: O(n*lon(n))  
    + Worst-case space complexity: О(n) total, O(n)  