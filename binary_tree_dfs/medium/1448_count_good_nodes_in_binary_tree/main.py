# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.count = 0

        def dfs(node: Optional[TreeNode], max_value: int):
            if not node:
                return

            if node.val >= max_value:
                self.count += 1
                max_value = node.val

            dfs(node.left, max_value)
            dfs(node.right, max_value)

        dfs(root, root.val)

        return self.count

if __name__ == "__main__":
    s = Solution()

    print(
        s.goodNodes(
            TreeNode(3,
                TreeNode(1,
                    TreeNode(3),
                ),
                TreeNode(4,
                    TreeNode(1),
                    TreeNode(5),
                ),
            )
        )
    )

    print(
        s.goodNodes(
            TreeNode(3,
                TreeNode(3,
                    TreeNode(4),
                    TreeNode(2),
                )
            )
        )
    )

    print(
        s.goodNodes(TreeNode(1))
    )
