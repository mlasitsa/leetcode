def validateCelebrity(potentialCeleb, n, knows):
    '''
    U - Understand:
    - Problem: Find the **celebrity** at a party with `n` people (0 to `n-1`).
      - A **celebrity** is someone who:
        1. **Is known by everyone** (all others know them).
        2. **Knows no one** (they don’t know anyone else).
      - We can use the `knows(a, b)` function which returns `True` if `a` knows `b`.

    - Constraints:
      - `1 <= n <= 100`
      - `knows(a, b)` runs in **O(1)** time.

    - Example:
      ```
      Input:
        n = 4
        knows(0, 1) -> True
        knows(0, 2) -> True
        knows(0, 3) -> True
        knows(1, 2) -> False
        knows(1, 3) -> False
        knows(2, 1) -> True
        knows(2, 3) -> True
        knows(3, 1) -> False
        knows(3, 2) -> False
      Output: 2
      ```

      Explanation:
      - Person **2** is known by **everyone** (0,1,3).
      - Person **2** **does not know** anyone else.
    
    Edge Cases:
    1. **No celebrity exists**: Everyone knows at least one other person.
    2. **All people know each other**: No single person meets both conditions.
    3. **Only one person exists (`n=1`)**: That person is trivially the celebrity.

    M - Match:
    - **Graph Representation**:
      - Each person is a node.
      - A **directed edge** from `a → b` means `a` knows `b`.
      - A **celebrity** has **no outgoing edges** and **incoming edges from all others**.

    - **Two-pass solution**:
      - **First Pass**: Identify a **potential** celebrity by checking if one exists that **doesn’t know anyone**.
      - **Second Pass**: Validate if this potential celebrity is **known by everyone**.

    P - Plan:
    1. **Find a potential celebrity (`potentialCeleb`)**:
       - Start with `potentialCeleb = 0`.
       - If `potentialCeleb` knows `i`, update `potentialCeleb = i`.
    2. **Validate `potentialCeleb`**:
       - Confirm that `potentialCeleb` does **not know** anyone.
       - Confirm that **everyone knows `potentialCeleb`**.
       - If either condition fails, return `-1`.
    3. **Return `potentialCeleb` if it satisfies conditions, else return `-1`**.

    I - Implement:
    '''
    for i in range(n):
        if potentialCeleb == i:
            continue
        # Celebrity must be known by everyone & must not know anyone.
        if not knows(i, potentialCeleb) or knows(potentialCeleb, i):
            return -1
    return potentialCeleb

def findCelebrity(n, knows):
    potentialCeleb = 0

    # Step 1: Identify a potential celebrity
    for i in range(1, n):
        if knows(potentialCeleb, i) and not knows(i, potentialCeleb):
            potentialCeleb = i

    # Step 2: Validate if `potentialCeleb` is a true celebrity
    return validateCelebrity(potentialCeleb, n, knows)


'''
Alternative Approach: Using Two Pointers
- Instead of a two-pass method, use **two-pointer elimination**.

P - Plan:
1. **Identify a potential celebrity (`candidate`)**:
   - Initialize `candidate = 0`.
   - Iterate over `n`, if `candidate` knows `i`, update `candidate = i`.
   - At the end, `candidate` is the only possible celebrity.
2. **Verify `candidate`**:
   - Ensure `candidate` does not know anyone.
   - Ensure everyone knows `candidate`.

I - Implement:
'''
def findCelebrityOptimized(n, knows): # Simply two functions in one
    candidate = 0

    # Step 1: Find a potential celebrity
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i

    # Step 2: Verify if candidate is a true celebrity
    for i in range(n):
        if i == candidate:
            continue
        if knows(candidate, i) or not knows(i, candidate):
            return -1

    return candidate

# Example Usage:
'''
E - Evaluate:
1. Input:
   n = 4
   knows(0, 1) -> True
   knows(0, 2) -> True
   knows(0, 3) -> True
   knows(1, 2) -> False
   knows(1, 3) -> False
   knows(2, 1) -> True
   knows(2, 3) -> True
   knows(3, 1) -> False
   knows(3, 2) -> False
   Output: 2

2. Edge Case:
   - Input: `n=3, knows(0,1)=True, knows(1,0)=True, knows(2,1)=False`
   - Output: `-1` (No celebrity exists).

Time Complexity:
- **O(n)**: We perform `O(n)` operations to find a potential celebrity.
- **O(n)**: We perform `O(n)` validation checks.
- **Total: O(n)** (Optimized version is O(n)).

Space Complexity:
- **O(1)**: Uses only a few integer variables.
'''
