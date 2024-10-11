# https://leetcode.com/problems/pascals-triangle/description

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the triangle with the first row
        triangle = [[1]]

        for i in range(1, numRows):
            # Create a new row with all 1s
            row = [1] * (i + 1)

            # Calculate the middle values of the row
            for j in range(1, i):
                # Each element is the sum of the two elements above it
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]

            # Add the completed row to the triangle
            triangle.append(row)

        return triangle

if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))
    print(s.generate(1))
