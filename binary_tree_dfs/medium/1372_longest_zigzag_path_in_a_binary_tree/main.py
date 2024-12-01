# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        LEFT = 0
        RIGHT = 1
        self.max_len = 0

        def dfs(node: Optional[TreeNode], direction: int, length: int):
            if not node:
                self.max_len = max(self.max_len, length)
                return

            self.max_len = max(self.max_len, length)

            if direction == LEFT:
                dfs(node.left, RIGHT, length + 1)
                dfs(node.right, LEFT, 1)
            else:
                dfs(node.right, LEFT, length + 1)
                dfs(node.left, RIGHT, 1)

        dfs(root, LEFT, 0)
        dfs(root, RIGHT, 0)

        return self.max_len - 1

if __name__ == "__main__":
    s = Solution()

    print(
        s.longestZigZag(
            TreeNode(1,
                None,
                TreeNode(1,
                    TreeNode(1),
                    TreeNode(1,
                        TreeNode(1,
                            None,
                            TreeNode(1,
                                None,
                                TreeNode(1),
                            ),
                        ),
                        TreeNode(1),
                    )
                )
            )
        )
    ) # 3

    print(
        s.longestZigZag(
            TreeNode(1,
                TreeNode(1,
                    None,
                    TreeNode(1,
                        TreeNode(1,
                            None,
                            TreeNode(1),
                        ),
                        TreeNode(1),
                    ),
                ),
                TreeNode(1),
            )
        )
    )

    print(
        s.longestZigZag(TreeNode(1))
    )
