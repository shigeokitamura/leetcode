# https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if sorted(word1) == sorted(word2):
            return True

        counter_word1 = Counter(word1)
        counter_word2 = Counter(word2)

        keys_word1 = sorted(counter_word1.keys())
        keys_word2 = sorted(counter_word2.keys())
        values_word1 = sorted(counter_word1.values())
        values_word2 = sorted(counter_word2.values())

        if (keys_word1 == keys_word2) and (values_word1 == values_word2):
            return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.closeStrings("abc", "bca")) # true
    print(s.closeStrings("a", "aa")) # false
    print(s.closeStrings("cabbba", "abbccc")) # true
    print(s.closeStrings("uau", "ssx")) # false
