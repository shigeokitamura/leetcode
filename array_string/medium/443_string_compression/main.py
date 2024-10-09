# https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed = ""

        prev_char = chars[0]
        count = 1

        for char in chars[1:]:
            if char == prev_char:
                count += 1
            else:
                compressed += prev_char
                if count > 1:
                    compressed += str(count)

                prev_char = char
                count = 1

        compressed += prev_char
        if count > 1:
            compressed += str(count)

        for i in range(len(compressed)):
            chars[i] = compressed[i]

        return len(compressed)


if __name__ == "__main__":
    s = Solution()
    print(s.compress(["a","a","b","b","c","c","c"])) # 6
    print(s.compress(["a"])) # 1
    print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])) # 4
