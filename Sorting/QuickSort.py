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
