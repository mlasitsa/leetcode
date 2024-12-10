# Bucket Sort Explanation:
# ------------------------
# How Bucket Sort Works:
# 1. **Determine the Range**: Find the maximum and minimum values in the array to define the range of the buckets.
# 2. **Create Buckets**: Divide the range into intervals (buckets) and allocate each element of the input array to the appropriate bucket based on its value.
# 3. **Sort Each Bucket**: Sort each bucket individually using a suitable sorting algorithm (e.g., Insertion Sort or Quick Sort). If the range of a bucket is small, sorting it is faster.
# 4. **Concatenate Buckets**: Combine all the sorted buckets to form the final sorted array.

# Why Bucket Sort is Helpful:
# - **Best for Uniformly Distributed Data**: Bucket Sort is particularly efficient when the input data is uniformly distributed across a known range.
# - **Linear Time Complexity (Under Ideal Conditions)**: When the data is uniformly distributed, and the range is appropriately divided into buckets, Bucket Sort can achieve O(n) time complexity.
# - **Parallelizable**: Since each bucket can be sorted independently, Bucket Sort can be parallelized, making it suitable for multi-threaded environments.
# - **Avoids Comparison Sorting**: Unlike comparison-based algorithms (like Merge Sort or Quick Sort), Bucket Sort leverages the distribution of data, which can be advantageous for certain datasets.

# Time Complexity:
# 1. **Creating Buckets and Distributing Elements**: O(n), as each element is placed into its respective bucket in one pass.
# 2. **Sorting Individual Buckets**: O(n) in the best case when the data is uniformly distributed, 
#    but can degrade to O(m log m) for poorly distributed data, where m is the size of the largest bucket.
# 3. **Combining Buckets**: O(n), as each bucket is concatenated in one pass.
# - **Overall Complexity**:
#    - Best Case: O(n + k), where n is the number of elements and k is the number of buckets.
#    - Worst Case: O(n^2), if all elements fall into a single bucket (rare in practice with good bucket design).

# Space Complexity:
# 1. **Buckets**: O(k), where k is the number of buckets.
# 2. **Additional Storage for Sorted Array**: O(n), the output array size.
# 3. **Total Space Complexity**: O(n + k).

# Advantages:
# - Efficient for sorting large datasets when the range of elements is known and evenly distributed.
# - Can achieve linear time complexity under ideal conditions.
# - Parallelizable for efficiency on multi-core systems.

# Disadvantages:
# - Not suitable for data with a wide range or when the range is unknown.
# - Additional space is required for buckets, making it less space-efficient than some in-place sorting algorithms like Quick Sort.
# - Performance is highly dependent on the bucket distribution. Poorly distributed data can degrade performance.

# Test array
testArray = [1, 2, 5, 1, 2, 10, 2, 3, 5, 6, 15, 17]

# Helper function to find the maximum value in the array
def findMax(array):
    maxNum = float('-inf')  # Start with the smallest possible number
    for num in array:
        maxNum = max(num, maxNum)  # Update maxNum if a larger number is found
    return maxNum

# Function to perform Bucket Sort
def bucketSort(arrayToSort):
    # Step 1: Find the maximum value in the array to determine the range of buckets
    n = findMax(arrayToSort)

    # Step 2: Create a "bucket array" where each index represents a possible value in the input
    bucketArray = [0] * (n + 1)  # Initialize buckets to 0
    sortedArray = []  # To store the sorted result

    # Step 3: Count the frequency of each number in the input array
    for num in arrayToSort:
        bucketArray[num] += 1  # Increment the count at the index corresponding to the number

    # Step 4: Reconstruct the sorted array from the bucket array
    for i in range(len(bucketArray)):  # Iterate through the buckets
        if bucketArray[i] == 0:  # Skip if the bucket is empty
            continue
        while bucketArray[i] != 0:  # Append the number `i` for each occurrence in the bucket
            sortedArray.append(i)
            bucketArray[i] -= 1  # Decrease the count in the bucket

    # Step 5: Return the sorted array
    return sortedArray

# Test the Bucket Sort implementation
print(bucketSort(testArray))
