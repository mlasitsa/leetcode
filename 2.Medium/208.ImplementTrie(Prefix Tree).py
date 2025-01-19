class Trie:
    """
    U - Understand the Problem
    Problem Statement:
    - Implement a Trie (prefix tree) with the following operations:
      1. `insert(word)`: Inserts a word into the trie.
      2. `search(word)`: Returns True if the word is in the trie, False otherwise.
      3. `startsWith(prefix)`: Returns True if any word in the trie starts with the given prefix.

    Clarifications/Constraints:
    - Words consist only of lowercase English letters.
    - Words and prefixes can be empty, but operations on empty inputs return False.
    - The trie should handle multiple insertions and searches efficiently.

    Examples:
    Input:
    trie = Trie()
    trie.insert("apple")
    trie.search("apple") -> True
    trie.search("app") -> False
    trie.startsWith("app") -> True
    trie.insert("app")
    trie.search("app") -> True

    Potential clarifying questions:
    1. Are the operations case-sensitive? (Yes, only lowercase English letters are considered.)
    2. Can words contain non-alphabetic characters? (No, only lowercase English letters.)
    """

    """
    M - Match with Patterns
    Pattern Identified:
    - Use a tree-like data structure where:
      * Each node represents a character.
      * Nodes at the end of words are marked as terminal nodes.
      * Prefix searches are efficient due to the hierarchical structure.
    """

    """
    P - Plan
    1. Use a dictionary to represent the children of each node.
    2. Each node should store:
       - `children`: A dictionary mapping characters to child nodes.
       - `isLast`: A boolean indicating if the node represents the end of a word.
    3. Implement methods:
       - `insert(word)`: Traverse the trie, creating nodes for new characters.
       - `search(word)`: Traverse the trie and check if the word ends at a terminal node.
       - `startsWith(prefix)`: Traverse the trie and check if the prefix exists.
    """

    def __init__(self):
        # Initialize the Trie with an empty dictionary and `isLast` as False
        self.children = {}
        self.isLast = False

    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.
        """
        root = self  # Start at the root of the trie

        for ch in word:
            if ch not in root.children:
                # Create a new node if the character is not present
                root.children[ch] = Trie()
            root = root.children[ch]  # Move to the child node

        # Mark the last node as a terminal node
        root.isLast = True

    def search(self, word: str) -> bool:
        """
        Search for a word in the trie.
        Returns True if the word is present and ends at a terminal node.
        """
        root = self  # Start at the root of the trie

        for ch in word:
            if ch not in root.children:
                return False  # Character not found, word doesn't exist
            root = root.children[ch]  # Move to the child node

        return root.isLast  # Return True if it's a terminal node, False otherwise

    def startsWith(self, prefix: str) -> bool:
        """
        Check if there is any word in the trie that starts with the given prefix.
        """
        root = self  # Start at the root of the trie

        for ch in prefix:
            if ch not in root.children:
                return False  # Character not found, prefix doesn't exist
            root = root.children[ch]  # Move to the child node

        return True  # Prefix exists in the trie


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
