# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels_idx: list[int] = []
        for idx, char in enumerate(s):
            if char in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
                vowels_idx.append(idx)

        reversed_vowels_idx = vowels_idx[::-1]
        for i in vowels_idx:
            s_list[i] = s[reversed_vowels_idx.pop(0)]

        return "".join(s_list)

if __name__ == "__main__":
    s = Solution()
    print(s.reverseVowels("IceCreAm"))
    print(s.reverseVowels("leetcode"))
