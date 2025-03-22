class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()  # Dummy head
        self.tail = Node()  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def removeFromList(self, node):
        """Removes a specific node from the doubly linked list."""
        if node == self.head or node == self.tail:
            return  # Do not remove dummy nodes

        node.prev.next = node.next  # Bypass `node`
        node.next.prev = node.prev  # Update backward link

        node.next = node.prev = None  # Help garbage collection
    
    def addToTheList(self, node):
        """Adds a node before the tail (Most Recently Used)."""
        prevNode = self.tail.prev  # Last real node before tail

        prevNode.next = node
        node.prev = prevNode

        node.next = self.tail
        self.tail.prev = node


class LRUCache:
    def __init__(self, capacity: int):
        '''
        U - Understand:
        - Problem: Design an LRU (Least Recently Used) cache that supports `get` and `put` operations in **O(1)** time complexity.
        - The cache should:
          1. Store at most `capacity` key-value pairs.
          2. When the cache reaches its capacity, remove the **least recently used (LRU)** key.
          3. `get(key)`: Return the value if the key exists, otherwise return `-1`.
          4. `put(key, value)`: Insert a new key-value pair or update an existing key.
             - If updating, move it to **most recently used (MRU)** position.
             - If inserting a new key and the cache is full, evict the **LRU** key.
        - Constraints:
          - `1 <= capacity <= 3000`
          - `0 <= key, value <= 10^4`

        M - Match:
        - **HashMap + Doubly Linked List (DLL)**:
          1. **HashMap (`cache`)**:
             - Stores `{key: node}` for **O(1)** lookup.
          2. **Doubly Linked List (`LRU`)**:
             - Maintains order of usage (leftmost = LRU, rightmost = MRU).
             - `addToTheList(node)`: Move a node to the **most recently used** position.
             - `removeFromList(node)`: Remove a node in **O(1)**.

        P - Plan:
        1. Initialize:
           - `cache`: Dictionary `{key: Node}` for fast lookups.
           - `LRU`: Doubly Linked List to track order of usage.
        2. `get(key)`:
           - If key exists:
             - Move node to **most recently used** position.
             - Return its value.
           - Else, return `-1`.
        3. `put(key, value)`:
           - If key exists:
             - Update value.
             - Move to **most recently used**.
           - Else:
             - Add new node to **most recently used**.
             - If capacity exceeded, remove **least recently used** node.

        I - Implement:
        '''
        self.capacity = capacity
        self.cache = {}  # HashMap to store key-node mapping
        self.LRU = DoublyLinkedList()

    def get(self, key: int) -> int:
        '''
        The key becomes the most recently used, so move it to the right (tail) of the linked list.
        Return the corresponding value from the HashMap.
        '''
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.LRU.removeFromList(node)
        self.LRU.addToTheList(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        '''
        If the key already exists, update its value and move it to most recently used (right).
        If the cache is full, remove the leftmost node (least recently used), which is at left.
        Insert the new key as most recently used (right).
        '''
        if key in self.cache:
            node = self.cache[key]  # Get the existing node
            self.LRU.removeFromList(node)  # Remove from current position
            node.value = value  # Update value
            self.LRU.addToTheList(node)  # Move it to the front (MRU)
        else:
            newNode = Node(value)  
            self.cache[key] = newNode
            self.LRU.addToTheList(newNode)

            if len(self.cache) > self.capacity:
                nodeToDelete = self.LRU.head.next  # Get the LRU node

                for k, v in self.cache.items():
                    if v == nodeToDelete:
                        del self.cache[k]
                        break  # Exit loop once found

                self.LRU.removeFromList(nodeToDelete) 

# Example Usage:
'''
E - Evaluate:
1. Input:
   cache = LRUCache(2)
   cache.put(1, 1)
   cache.put(2, 2)
   cache.get(1) -> 1 (Moves 1 to MRU)
   cache.put(3, 3) (Evicts 2, because it’s LRU)
   cache.get(2) -> -1 (2 was evicted)
   cache.get(3) -> 3 (3 is still in cache)

2. Input:
   cache = LRUCache(1)
   cache.put(1, 1)
   cache.put(2, 2) (Evicts 1)
   cache.get(1) -> -1
   cache.get(2) -> 2

Time Complexity:
- **O(1)** for `get()`: HashMap lookup + DLL operation.
- **O(1)** for `put()`: HashMap insert/update + DLL operation.

Space Complexity:
- **O(capacity)**: Stores at most `capacity` nodes.

Alternative Approach:
- **Using `OrderedDict` from `collections` (Python built-in LRU)**
- `OrderedDict` maintains order and provides **O(1)** operations.
'''




# MORE EFFICIENT VERSION OF CODE 

# ========================================
# U - Understand the Problem
# ========================================
# Problem Statement:
# Implement a Least Recently Used (LRU) Cache with the following operations in O(1) time:
# - get(key): Return the value if the key exists, otherwise return -1.
# - put(key, value): Insert or update the value. If the cache exceeds capacity, evict the least recently used item.

# Constraints:
# - The cache should always maintain the "most recently used" (MRU) at one end and "least recently used" (LRU) at the other.
# - You should implement the data structure yourself (not use Python's OrderedDict or similar).

# Clarifying Questions:
# - Can keys or values be negative? (Yes, we assume any integers are valid.)
# - What happens when multiple gets happen on the same key? (It should be moved to MRU end.)
# - If a key is updated, is it considered recently used? (Yes.)

# Example:
# cache = LRUCache(2)
# cache.put(1, 1)  # cache = {1=1}
# cache.put(2, 2)  # cache = {1=1, 2=2}
# cache.get(1)     # returns 1, cache = {2=2, 1=1}
# cache.put(3, 3)  # evicts key 2, cache = {1=1, 3=3}
# cache.get(2)     # returns -1 (not found)
# cache.put(4, 4)  # evicts key 1, cache = {3=3, 4=4}
# cache.get(1)     # returns -1
# cache.get(3)     # returns 3
# cache.get(4)     # returns 4

# ========================================
# M - Match with Patterns
# ========================================
# Pattern: HashMap + Doubly Linked List
# - HashMap provides O(1) access to cache nodes by key.
# - Doubly Linked List allows O(1) addition and deletion of nodes (for tracking LRU/MRU order).
# - Dummy head/tail nodes simplify pointer logic for edge cases.

# ========================================
# P - Plan
# ========================================
# Classes:
# 1. Node: Stores key, value, and pointers to previous and next nodes.
# 2. DoubleLinkedList: Manages dummy head and tail, and supports add/delete operations.
# 3. LRUCache:
#    - get(key): If key exists, move node to front (MRU) and return its value.
#    - put(key, value): 
#        - If key exists, update value, move node to MRU.
#        - If key doesn't exist:
#            - If at capacity: evict LRU node from back.
#            - Add new node to front and update hashmap.

# ========================================
# I - Implement
# ========================================
class Node:
    def __init__(self, key, val, prev=None, nexT=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nexT = nexT


class DoubleLinkedList:
    def __init__(self):
        self.start = Node(None, None)  # Dummy start (MRU side)
        self.end = Node(None, None)    # Dummy end (LRU side)
        self.end.nexT = self.start
        self.start.prev = self.end

    def add(self, node):
        # Add new node to front (before dummy start)
        prevNode = self.start.prev
        node.prev = prevNode
        node.nexT = self.start
        prevNode.nexT = node
        self.start.prev = node

    def delete(self, node):
        # Remove node from list
        prevNode = node.prev
        nextNode = node.nexT
        prevNode.nexT = nextNode
        nextNode.prev = prevNode


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = {}  # Key -> Node
        self.doubleList = DoubleLinkedList()

    def get(self, key) -> int:
        if key in self.storage:
            node = self.storage[key]
            self.doubleList.delete(node)
            self.doubleList.add(node)  # Move to front
            return node.val
        else:
            return -1

    def put(self, key, value) -> None:
        if key in self.storage:
            node = self.storage[key]
            node.val = value
            self.doubleList.delete(node)
            self.doubleList.add(node)  # Refresh MRU status
        else:
            if len(self.storage) == self.capacity:
                lru_node = self.doubleList.end.nexT  # Least recently used node
                if lru_node.key is not None:
                    self.doubleList.delete(lru_node)
                    del self.storage[lru_node.key]
            newNode = Node(key, value)
            self.doubleList.add(newNode)
            self.storage[key] = newNode

# ========================================
# R - Review
# ========================================
# - get(key) and put(key, value) both run in O(1) time.
# - The linked list guarantees fast removal and insertion of nodes.
# - HashMap provides constant lookup for keys.

# ========================================
# E - Evaluate
# ========================================
# Time Complexity:
# - get, put: O(1) each

# Space Complexity:
# - O(N) for HashMap
# - O(N) for linked list nodes
# - Total: O(N), where N = capacity

# Edge Cases:
# - Capacity = 0 (all puts will evict immediately)
# - Repeated puts on the same key (should just update and refresh position)
# - get on non-existent key returns -1
