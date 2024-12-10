# Quick Sort Explanation:
# ------------------------
# How Quick Sort Works:
# 1. **Pivot Selection**: Choose a pivot element from the array (commonly the last element, but other strategies can also be used).
# 2. **Partitioning**: Divide the array into two sub-arrays:
#    - Left sub-array: Contains elements less than the pivot.
#    - Right sub-array: Contains elements greater than the pivot.
# 3. **Recursive Sorting**: Recursively apply Quick Sort to the left and right sub-arrays.
# 4. **Combine**: Combine the sorted left sub-array, the pivot, and the sorted right sub-array.

# Why Quick Sort is Helpful:
# - **Efficient for Large Datasets**: Quick Sort is faster than many other sorting algorithms (like Merge Sort) for in-memory sorting due to its smaller constant factors.
# - **In-Place Sorting**: Can be implemented in-place, requiring less space compared to Merge Sort.
# - **Highly Optimizable**: By choosing an appropriate pivot (e.g., median-of-three), Quick Sort's performance can be further improved.

# Time Complexity:
# - Best Case: O(n log n), when the pivot divides the array into roughly equal parts.
# - Average Case: O(n log n), on random data distributions.
# - Worst Case: O(n^2), when the pivot repeatedly divides the array into one large and one empty sub-array (e.g., already sorted array with poor pivot selection).

# Space Complexity:
# - O(log n) for the recursion stack in the best and average cases.
# - O(n) in the worst case due to deep recursion.

# Advantages:
# - Faster than many other algorithms for most datasets.
# - Can be implemented in-place, making it space-efficient.

# Disadvantages:
# - Performance is heavily dependent on pivot selection.
# - Worst-case time complexity is O(n^2), which can occur with poor pivot selection.


arrayToSort = [1, 3, 5, 6, 7, 9, 10, 2, 3, 1, 15, 21, 4]

def lessThanPivot(array, pivot):
    arr = []
    for num in array:
        if num < pivot:  # Strictly less than pivot
            arr.append(num)
    return arr

def moreThanPivot(array, pivot):
    arr = []
    for num in array:
        if num > pivot:
            arr.append(num)
    return arr

def quickSort(array):
    if len(array) <= 1:  # Base case
        return array
    
    pivot = array[-1]  # Select last element as pivot
    
    # Divide into sublists
    left = quickSort(lessThanPivot(array[:-1], pivot))  # Exclude the pivot itself
    right = quickSort(moreThanPivot(array[:-1], pivot))
    
    return left + [pivot] + right

print(quickSort(arrayToSort))
