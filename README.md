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