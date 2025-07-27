"""
### **UMPIRE Framework for `isAnagram`**

#### **U - Understand the Problem**
We are given two strings, `s` and `t`, and we need to determine whether `t` is an anagram of `s`.  
A valid anagram means:
- Both strings should have the **same characters** in **equal frequency** but possibly in different order.

##### **Clarifying Questions**
1. **Can `s` and `t` contain spaces or special characters?**
   - No, we assume lowercase English letters only.
2. **Do we need to consider case sensitivity?**
   - No, all characters are lowercase.
3. **What if both strings are empty?**
   - They are anagrams (`"" == ""` → `True`).
4. **Can we use sorting?**
   - Yes, but sorting takes **O(N log N)** time. A more optimal approach is using **hashmaps**.

---

#### **M - Map the Input to the Output**
##### **Example 1**
```python
s = "anagram"
t = "nagaram"
```
- Frequency of `s`: `{a: 3, n: 1, g: 1, r: 1, m: 1}`
- Frequency of `t`: `{n: 1, a: 3, g: 1, r: 1, m: 1}`
- **Output:** `True` ✅

##### **Example 2**
```python
s = "rat"
t = "car"
```
- Frequency of `s`: `{r: 1, a: 1, t: 1}`
- Frequency of `t`: `{c: 1, a: 1, r: 1}`
- **Output:** `False` ❌

---

#### **P - Plan**
1. **Edge Cases:**
   - If `len(s) != len(t)`, return `False` immediately.
   - If both strings are empty, return `True`.
2. **Use a HashMap (Dictionary):**
   - **Step 1:** Count occurrences of each character in `s` and store in a hashmap.
   - **Step 2:** Traverse `t` and **decrement the count** of each character from the hashmap.
   - **Step 3:** If any character's count goes **below zero**, return `False`.
   - **Step 4:** If all checks pass, return `True`.

---

#### **I - Implement**
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}

        if len(s) != len(t):
            return False

        # Count frequency of characters in s
        for ch in s:
            if ch in hmap:
                hmap[ch] += 1
            else:
                hmap[ch] = 1
        
        # Decrement frequency based on t
        for ch in t:
            if ch not in hmap:
                return False  # Extra character in t
            if hmap[ch] <= 0:
                return False  # More occurrences in t than in s
            hmap[ch] -= 1
        
        return True
```

---
"""
#### **R - Review (Optimize & Edge Cases)**
##### **Time Complexity**
- **Building the hashmap:** `O(N)`
- **Traversing `t` to decrement counts:** `O(N)`
- **Total Complexity:** **`O(N)`** (efficient compared to sorting `O(N log N)`)

##### **Space Complexity**
- **Hashmap stores at most 26 keys (`O(1)`)** since there are only lowercase letters.
- **Best-case scenario:** `O(1)`, worst case **`O(N)`**.

##### **Edge Cases Considered**
✅ `s = "a"`, `t = "b"` → `False`  
✅ `s = "apple"`, `t = "ppale"` → `True`  
✅ `s = "abcd"`, `t = "abcde"` → `False` (Different lengths)  
✅ `s = "abc"`, `t = "cba"` → `True`  

---
"""

# Alternative Solution: Sorting (O(N log N))


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)  # Sorting both strings and comparing




