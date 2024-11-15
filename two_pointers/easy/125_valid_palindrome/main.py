# https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        left = 0
        right = len(s) - 1

        while(left < right):
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

if __name__ == "__main__":
    s = Solution()

    print(s.isPalindrome("A man, a plan, a canal: Panama")) # True
    print(s.isPalindrome("race a car")) # False
    print(s.isPalindrome(" ")) # True