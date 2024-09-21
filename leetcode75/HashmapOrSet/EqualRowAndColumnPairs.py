class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        '''
        so this is a matrix problem where we need to traverse carefully

        to move through each row, we do:
        for r in range(grid):
            for c in range(grid[r]):
                storing elements to a set

        for c in range(len(grid[0])):  # Iterate through columns (assuming non-empty grid)
            for r in range(len(grid)):  # Iterate through rows of the current column
                store elements  # Store elements in a set

        we need to store elements as a tuple since we cannot insert list into a hmap, 
        then tricky part is when we are traversing through 2 hmaps, we need to actually multiply values, 
        since 2 same rows would be equal one column twice
        '''
        row_map = {}  # Hashmap to store row tuples and their counts
        col_map = {}  # Hashmap to store column tuples and their counts
        count = 0     # To store the final count of matching row-column pairs

        # Step 1: Traverse matrix by row and store in row_map
        for r in range(len(grid)):
            arr = []  # Temporary list to store row elements
            for c in range(len(grid[r])):  # Traverse each column in the row
                arr.append(grid[r][c])  # Append element to list
            row_tuple = tuple(arr)  # Convert list to tuple (for hashing)
            
            # Add row_tuple to row_map, or increment its count if it already exists
            if row_tuple in row_map:
                row_map[row_tuple] += 1
            else:
                row_map[row_tuple] = 1

        # Step 2: Traverse matrix by column and store in col_map
        for c in range(len(grid[0])):  # Loop over each column index
            arr = []  # Temporary list to store column elements
            for r in range(len(grid)):  # Traverse each row in the column
                arr.append(grid[r][c])  # Append element to list
            col_tuple = tuple(arr)  # Convert list to tuple (for hashing)

            # Add col_tuple to col_map, or increment its count if it already exists
            if col_tuple in col_map:
                col_map[col_tuple] += 1
            else:
                col_map[col_tuple] = 1

        # Step 3: Compare row_map and col_map to count matching row-column pairs
        
        for row_tuple in row_map:
            if row_tuple in col_map:
                # Multiply the counts of matching row_tuple and col_tuple
                count += row_map[row_tuple] * col_map[row_tuple]

        return count


sol = Solution
res = sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]])

if res == 1:
    print("Good Job") 
else:
    print("Try again...")