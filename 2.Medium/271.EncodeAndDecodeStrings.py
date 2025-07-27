class Solution:

    """
    U - Understand the Problem
    Problem Statement:
    - Design two methods:
      1. `encode`: Encodes a list of strings into a single string.
      2. `decode`: Decodes the encoded string back into a list of strings.
    - The encoding format should handle edge cases such as empty strings and strings containing special characters.

    Clarifications/Constraints:
    - Strings can contain any characters, including delimiters like '|'.
    - The decoding process should perfectly reconstruct the original list of strings.
    - Input and output are guaranteed to be valid according to the encode/decode format.

    Examples:
    Input: ["hello", "world"]
    Output: "hello|world|" (encoded string)
    Decoded Output: ["hello", "world"]

    Input: ["a|b", "c"]
    Output: "a|b||c|" (encoded string)
    Decoded Output: ["a|b", "c"]
    """

    """
    M - Match with Patterns
    Pattern Identified:
    - Use a delimiter-based encoding where each string is concatenated with a special delimiter.
    - To handle cases where strings may contain the delimiter, include the string length as metadata.
    """

    """
    P - Plan
    Encoding:
    1. For each string, prepend its length and a special character (e.g., ':').
    2. Concatenate all strings into a single encoded string.

    Decoding:
    1. Parse the encoded string by reading the length of each string.
    2. Extract the string of the given length and append it to the result list.
    """

    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings into a single string.
        """
        result = ''
        for word in strs:
            result += f"{len(word)}:{word}"  # Add length and the string itself
        return result

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string into a list of strings.
        """
        result = []
        i = 0

        while i < len(s):
            # Find the length of the next string
            j = s.find(':', i)
            length = int(s[i:j])
            i = j + 1  # Move past the colon
            result.append(s[i:i + length])  # Extract the string of the given length
            i += length  # Move to the next encoded string

        return result

# Example Usage
"""
E - Evaluate
Test the solution with examples:
1. Input: ["hello", "world"] -> Encoded: "5:hello5:world", Decoded: ["hello", "world"]
2. Input: ["a|b", "c"] -> Encoded: "3:a|b1:c", Decoded: ["a|b", "c"]
3. Input: [""] -> Encoded: "0:", Decoded: [""]

Edge Cases:
1. Empty list -> Encoded: "", Decoded: [].
2. Strings with special characters -> Properly handle lengths to avoid misinterpretation.
"""

# Test cases
sol = Solution()
# Encode examples
encoded = sol.encode(["hello", "world"])
print("Encoded:", encoded)  # Output: "5:hello5:world"
decoded = sol.decode(encoded)
print("Decoded:", decoded)  # Output: ["hello", "world"]

# Edge cases
encoded = sol.encode(["a|b", "c"])
print("Encoded:", encoded)  # Output: "3:a|b1:c"
decoded = sol.decode(encoded)
print("Decoded:", decoded)  # Output: ["a|b", "c"]

encoded = sol.encode([""])
print("Encoded:", encoded)  # Output: "0:"
decoded = sol.decode(encoded)
print("Decoded:", decoded)  # Output: [""]
