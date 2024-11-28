# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], depth: int):
            if not root:
                return depth

            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)

if __name__ == "__main__":
    s = Solution()

    print(
        s.maxDepth(
            TreeNode(
                3,
                TreeNode(9),
                TreeNode(
                    20,
                    TreeNode(15),
                    TreeNode(7),
                )
            )
        )
    ) # 3

    print(
        s.maxDepth(
            TreeNode(
                1,
                None,
                TreeNode(2),
            )
        )
    ) # 2
