class TimeMap:
    def __init__(self):
        """
        U - Understand the Problem
        Problem:
        - Implement a time-based key-value store.
        - You can store multiple values for the same key at different timestamps.
        - When calling `get(key, timestamp)`, return the value associated with `key` at the largest timestamp <= given timestamp.

        Clarifications:
        - If there’s no such timestamp, return "".
        - Timestamps are strictly increasing for the same key (guaranteed by problem).
        - How many operations? (Up to 2 * 10^5 for set and get combined.)

        M - Match
        - This is a dictionary-based caching problem.
        - We store all [timestamp, value] pairs for each key.
        - Binary Search fits perfectly for fast retrieval based on timestamp.
        """

        self.hmap = {}  # Key: str -> Value: List of [timestamp, value] pairs

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        P - Plan
        - If key is not in hashmap, initialize a list for it.
        - Append the [timestamp, value] since timestamps are increasing.
        """
        if key not in self.hmap:
            self.hmap[key] = []
        self.hmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        """
        P - Plan
        - If key doesn't exist, return ""
        - Perform binary search on timestamp to find largest ts <= given timestamp.
        - Return the corresponding value if found.
        """

        if key not in self.hmap:
            return ''  # No values stored for this key

        arr = self.hmap[key]
        left, right = 0, len(arr) - 1
        res = ""  # Default result if no valid timestamp found

        # I - Implement (Binary Search)
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]  # Exact match found
            elif arr[mid][0] < timestamp:
                res = arr[mid][1]  # Potential candidate
                left = mid + 1     # Look for a closer/larger timestamp
            else:
                right = mid - 1    # Look left (timestamp too large)
        
        return res  # Best candidate found during search

        """
        R - Review
        - We're guaranteed that timestamps are in order — which enables binary search.
        - Each `set` operation is O(1), and each `get` operation is O(log n).

        E - Evaluate
        Time Complexity:
        - `set` is O(1)
        - `get` is O(log n) where n is number of entries for the given key

        Space Complexity:
        - O(n): We're storing every [timestamp, value] pair per key

        Edge Cases:
        - get("foo", 100) with no `set` → returns ""
        - Multiple sets with same key at increasing timestamps work fine
        """
