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
