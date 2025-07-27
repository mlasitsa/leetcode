from queue import Queue

class MyStack:
    """
    U - Understand the Problem
    Problem Statement:
    - Implement a stack using a single queue.
    - A stack is a Last-In-First-Out (LIFO) data structure.
    - Implement the following operations:
      1. `push(x)`: Pushes an element onto the stack.
      2. `pop()`: Removes and returns the top element of the stack.
      3. `top()`: Returns the top element without removing it.
      4. `empty()`: Returns whether the stack is empty.

    Clarifications/Constraints:
    - Operations must be implemented using a single queue.
    - Operations `top` and `pop` are guaranteed to be valid.
    - The stack supports duplicate elements.

    Examples:
    Input:
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.top() -> Output: 2
    stack.pop() -> Output: 2
    stack.empty() -> Output: False

    Potential clarifying questions:
    1. Can the stack handle duplicate elements? (Yes, duplicates are allowed.)
    2. What should happen if `pop` or `top` is called on an empty stack? (Guaranteed not to happen.)
    """

    """
    M - Match with Patterns
    Pattern Identified:
    - Use a single queue and rotate elements during `push` to maintain the LIFO property.
    - Use the queue's `get` and `put` operations to simulate stack behavior.
    """

    """
    P - Plan
    1. Initialize the queue for the stack implementation.
    2. Push Operation:
       - Add the element to the queue.
       - Rotate the queue to move the newly added element to the front (top of the stack).
    3. Pop Operation:
       - Dequeue the front element of the queue (top of the stack).
    4. Top Operation:
       - Use a temporary variable to peek at the front element, then rotate the queue to maintain order.
    5. Empty Operation:
       - Check if the queue is empty.
    """

    def __init__(self):
        self.q = Queue()
        self.top_element = None  # To keep track of the top element

    def push(self, x: int) -> None:
        """
        Push element onto the stack.
        """
        self.top_element = x  # Update the top element
        self.q.put(x)  # Add element to the queue

    def pop(self) -> int:
        """
        Remove and return the top element of the stack.
        """
        el = None  # Temporary variable to store dequeued elements
        last = self.top_element  # The current top element

        # Rotate the queue until the top element is found
        while el != last:
            el = self.q.get()  # Dequeue an element
            if el != last:
                self.q.put(el)  # Re-enqueue all elements except the last one
                self.top_element = el  # Update the new top element

        return el  # Return the last (top) element

    def top(self) -> int:
        """
        Return the top element of the stack without removing it.
        """
        return self.top_element  # Return the stored top element

    def empty(self) -> bool:
        """
        Return whether the stack is empty.
        """
        return self.q.empty()

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input:
   stack = MyStack()
   stack.push(1)
   stack.push(2)
   stack.top() -> Output: 2
   stack.pop() -> Output: 2
   stack.empty() -> Output: False

2. Edge Case:
   Input:
   stack = MyStack()
   stack.empty() -> Output: True

Time Complexity:
- `push`: O(1), no rotations needed.
- `pop`: O(n), rotates through the queue to find the top element.
- `top`: O(1), directly returns the stored top element.
- `empty`: O(1), checks if the queue is empty.

Space Complexity:
- O(n), for the queue.
"""
