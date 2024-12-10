# Merge Sort Explanation:
# ------------------------
# How Merge Sort Works:
# 1. **Divide**: Recursively divide the array into two halves until each sub-array contains only one element.
# 2. **Conquer**: Merge two sorted sub-arrays back into a single sorted array. This involves comparing elements from the two sub-arrays and placing them in the correct order in a temporary array.
# 3. **Combine**: Continue merging until all sub-arrays are merged into one fully sorted array.

# Why Merge Sort is Helpful:
# - **Guaranteed O(n log n)**: Merge Sort always runs in O(n log n), making it more predictable than Quick Sort, which can degrade to O(n^2) in the worst case.
# - **Stable Sorting Algorithm**: Maintains the relative order of equal elements, which is useful in certain applications.
# - **External Sorting**: Ideal for sorting large datasets that don't fit into memory, as it can work with smaller chunks and merge them.

# Time Complexity:
# - Divide the array: O(log n) for the recursive calls.
# - Merge operation: O(n) for merging two sorted arrays.
# - Overall Complexity: O(n log n)

# Space Complexity:
# - Requires O(n) additional space for temporary arrays during the merging process.
# - Not in-place, as additional storage is needed for the sub-arrays.

# Advantages:
# - Predictable performance with guaranteed O(n log n).
# - Efficient for large datasets.
# - Stable sort.

# Disadvantages:
# - Requires additional memory (O(n)) for merging, which can be a drawback for memory-constrained systems.
# - Slower than in-place algorithms like Quick Sort for smaller datasets due to overhead.


D = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def merge_sort(arr):
  n = len(arr)

  if n == 1:
    return arr

  m = len(arr) // 2
  L = arr[:m]
  R = arr[m:]

  L = merge_sort(L)
  R = merge_sort(R)
  l, r = 0, 0
  L_len = len(L)
  R_len = len(R)

  sorted_arr = [0] * n
  i = 0

  while l < L_len and r < R_len:
    if L[l] < R[r]:
      sorted_arr[i] = L[l]
      l += 1
    else:
      sorted_arr[i] = R[r]
      r += 1

    i += 1

  while l < L_len:
    sorted_arr[i] = L[l]
    l += 1
    i += 1

  while r < R_len:
    sorted_arr[i] = R[r]
    r += 1
    i += 1

  return sorted_arr

print(merge_sort(D))