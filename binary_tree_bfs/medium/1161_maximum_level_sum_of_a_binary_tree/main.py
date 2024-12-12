# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level_sums = []

        while queue:
            tmp = deque()
            level_sum = 0

            for node in queue:
                level_sum += node.val

                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)

            queue = tmp
            level_sums.append(level_sum)

        max_sum = -10 ** 5
        max_sum_idx = 0
        for idx in range(len(level_sums)):
            level_sum = level_sums[idx]
            if level_sum > max_sum:
                max_sum = level_sum
                max_sum_idx = idx
        print(level_sums)
        return max_sum_idx + 1

if __name__ == "__main__":
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(0)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(-8)
    print(s.maxLevelSum(root)) # 2

    root = TreeNode(989)
    root.right = TreeNode(10250)
    root.right.left = TreeNode(98693)
    root.right.right = TreeNode(-89388)
    root.right.right.right = TreeNode(-32127)
    print(s.maxLevelSum(root)) # 2

    root = TreeNode(-100)
    root.left = TreeNode(-200)
    root.right = TreeNode(-300)
    root.left.left = TreeNode(-20)
    root.left.right = TreeNode(-5)
    root.right.left = TreeNode(-10)
    print(s.maxLevelSum(root)) # 3
