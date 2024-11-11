# https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        string = ""
        num = 0

        for char in s:
            if char == "[":
                stack.append(string)
                stack.append(num)

                string = ""
                num = 0
            elif char == "]":
                stack_num = stack.pop()
                prev_string = stack.pop()
                string = prev_string + stack_num * string
            elif char.isdigit():
                num = num * 10 + int(char)
            else:
                string += char

        return string

if __name__ == "__main__":
    s = Solution()

    print(s.decodeString("3[a]2[bc]")) # "aaabcbc"
    print(s.decodeString("3[a2[c]]")) # "accaccacc"
    print(s.decodeString("2[abc]3[cd]ef")) # "abcabccdcdcdef"
