class Solution:
    def decodeString(self, s: str) -> str:

        num_stack = []      # Stack to store numbers (k)
        str_stack = []      # Stack to store substrings
        current_str = ""    # Current substring being built
        current_num = 0     # Current number being built

        for char in s:
            if char.isdigit():
                # Build the number, since it can be more than one digit (e.g., 12[a])
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current number and string to their respective stacks
                num_stack.append(current_num)
                str_stack.append(current_str)
                # Reset current_str and current_num for the next encoded part
                current_str = ""
                current_num = 0
            elif char == ']':
                # Pop the number and the string from stacks
                repeat_num = num_stack.pop()
                last_str = str_stack.pop()
                # Repeat the current string and append it to the last string
                current_str = last_str + current_str * repeat_num
            else:
                # Build the current string
                current_str += char

        return current_str


sol = Solution()
res = sol.decodeString("3[a]2[bc]")

if res == 'aaabcbc':
    print('Good Job')
else:
    print('Try again')
    print('Your res is', res)