class MyQueue:
    def __init__(self):
        self.stack1 = []  # Input stack
        self.stack2 = []  # Output stack
        self.front = None  # To track the front element

    """
    U - Understand the Problem
    Problem Statement:
    - Implement a queue using two stacks.
    - The queue should support:
      1. `push(x)`: Insert an element into the queue.
      2. `pop()`: Remove the front element from the queue.
      3. `peek()`: Return the front element without removing it.
      4. `empty()`: Check if the queue is empty.

    Constraints:
    - Only standard stack operations (push, pop, top/peek, empty) can be used.
    - We must maintain FIFO (First-In-First-Out) behavior using LIFO (Last-In-First-Out) stacks.
    - The operations should be efficient

    Examples:
    Input:
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        queue.peek() -> Output: 1
        queue.pop() -> Output: 1
        queue.empty() -> Output: False
    """

    """
    M - Match with Patterns
    Observations:
    - This is a **queue simulation using two stacks**.
    - A queue follows **FIFO**, while a stack follows **LIFO**.
    - **Reversing a stack gives FIFO order**, so we need:
      - **Stack1** for pushing new elements.
      - **Stack2** for popping elements in queue order.

    Two Approaches:
    1. **Costly push**: Reorder elements every time we push.
    2. ✅ **Costly pop (more optimal)**: Transfer elements from stack1 to stack2 when needed.
    """

    """
    P - Plan
    **Approach (Efficient pop)**
    1. **Push(x)**:
       - If stack1 is empty, store `x` as `front` (for efficient peek).
       - Push `x` onto stack1.

    2. **Pop()**:
       - If stack2 is empty, transfer all elements from stack1 to stack2.
       - Pop from stack2.

    3. **Peek()**:
       - If stack2 is not empty, return `stack2[-1]`.
       - Otherwise, return `front` (oldest element stored).

    4. **Empty()**:
       - Queue is empty if **both stack1 and stack2 are empty**.
    """

    def push(self, x: int) -> None:
        """Insert element into queue."""
        if not self.stack1:
            self.front = x  # Store first element for peek
        self.stack1.append(x)

    def pop(self) -> int:
        """Remove and return front element of queue."""
        if not self.stack2:  # Move elements only if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()  # Pop from stack2 (O(1))

    def peek(self) -> int:
        """Return front element of queue without removing it."""
        if self.stack2:
            return self.stack2[-1]  # Front of queue is top of stack2
        return self.front  # If stack2 is empty, return stored front

    def empty(self) -> bool:
        """Check if queue is empty."""
        return not self.stack1 and not self.stack2

    """
    R - Review
    - Uses two stacks efficiently.
    - Minimizes redundant moves between stacks.
    - Ensures O(1) amortized time for all operations.
    - Stores the front element to optimize `peek()`.
    """

    """
    E - Evaluate
    Time Complexity:
    - Push: O(1) (Always appends to stack1)
    - Pop: Amortized O(1) (Transfers stack1 to stack2 only when needed)
    - Peek: O(1) (Direct access)
    - Empty: O(1) (Checks two stacks)

    Space Complexity:
    - O(N) (Two stacks store at most `N` elements)

    Edge Cases:
    1. Empty queue (pop/peek should return valid results).
    2. Single element in queue.
    3. Pushing multiple elements, then popping all.
    4. Alternating push/pop calls.

    Optimizations:
    - Avoids unnecessary stack reversals.
    - Stores the front element for faster peek.
    """
