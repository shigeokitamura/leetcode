# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]

        window_vowels = 0
        for char in s[:k]:
            if char in vowels:
                window_vowels += 1
        max_vowels = window_vowels

        for i in range(k, len(s)):
            if s[i] in vowels:
                window_vowels += 1
            if s[i-k] in vowels:
                window_vowels -= 1
            max_vowels = max(max_vowels, window_vowels)

        return max_vowels


if __name__ == "__main__":
    s = Solution()
    print(s.maxVowels("abciiidef", 3)) # 3
    print(s.maxVowels("aeiou", 2)) # 2
    print(s.maxVowels("leetcode", 3)) # 2
    print(s.maxVowels("tryhard", 4)) # 1
