# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        count = 0
        for char in t:
            if char == s[count]:
                count += 1
                if count == len(s):
                    return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence(s="abc", t="ahbgdc")) # True
    print(s.isSubsequence(s="axc", t="ahbgdc")) # False
