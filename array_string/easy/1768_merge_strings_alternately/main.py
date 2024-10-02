# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1 = len(word1)
        len_word2 = len(word2)
        length = max(len_word1, len_word2)

        result = ""

        for i in range(length):
            if i < len_word1:
                result += word1[i]
            if i < len_word2:
                result += word2[i]

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.mergeAlternately("abc", "pqr"))
    print(s.mergeAlternately("ab", "pqrs"))
    print(s.mergeAlternately("abcd", "pq"))
