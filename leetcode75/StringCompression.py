class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1  # Starting count

        for i in range(len(chars) - 1, 0, -1):  # Start from second to last element
            char = chars[i]

            # Edge case when we reach the beginning
            if chars[i - 1] == char and i == 1:
                count += 1
                if count > 1:
                    if count >= 10:
                        bigNum = str(count)
                        p = 1  # Start `p` from 1
                        while p <= len(bigNum):
                            chars.insert(i + p, bigNum[p - 1])  # Insert digits at the correct position
                            p += 1
                    else:
                        chars.insert(i + 1, str(count))
                    count = 1

            # Corrected indexing and comparison
            if chars[i - 1] == char:  # Compare the current character with the previous one
                count += 1
                chars.pop(i)  # Remove the duplicate character

            elif chars[i - 1] != char:
                if count > 1:
                    if count >= 10:
                        bigNum = str(count)
                        p = 1  # Start `p` from 1
                        while p <= len(bigNum):
                            chars.insert(i + p, bigNum[p - 1])  # Insert digits at the correct position
                            p += 1
                    else:
                        chars.insert(i + 1, str(count))
                    count = 1

        return len(chars)


            
sol = Solution()
res = sol.compress(["a","a","b","b","c","c","c"])
if res = 6:
    print("Good Job")
else:
    print("Try Again...")