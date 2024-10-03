# https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2) != (str2 + str1):
            return ""

        len_str1 = len(str1)
        len_str2 = len(str2)
        gcd = 0

        if (len_str1 > len_str2):
            gcd = math.gcd(len_str1, len_str2)
        else:
            gcd = math.gcd(len_str2, len_str1)

        return str1[0:gcd]

if __name__ == "__main__":
    s = Solution()
    print(s.gcdOfStrings("ABCABC", "ABC")) # "ABC"
    print(s.gcdOfStrings("ABABAB", "ABAB")) # "AB"
    print(s.gcdOfStrings("LEET", "CODE")) # ""
