# https://leetcode.com/problems/leaf-similar-trees/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_sequence = []

        def dfs(root):
            if root == None:
                return

            if root.left == None and root.right == None:
                leaf_sequence.append(root.val)

                return

            dfs(root.left)
            dfs(root.right)

        dfs(root1)

        leaf_sequence_1 = leaf_sequence
        leaf_sequence = []

        dfs(root2)

        return leaf_sequence_1 == leaf_sequence

if __name__ == "__main__":
    s = Solution()

    print(
        s.leafSimilar(
            TreeNode(3,
                TreeNode(5,
                    TreeNode(6),
                    TreeNode(2,
                        TreeNode(7),
                        TreeNode(4),
                    )
                ),
                TreeNode(1,
                    TreeNode(9),
                    TreeNode(8),
                ),
            ),
            TreeNode(3,
                TreeNode(5,
                    TreeNode(6),
                    TreeNode(7),
                ),
                TreeNode(1,
                    TreeNode(4),
                    TreeNode(2,
                        TreeNode(9),
                        TreeNode(8),
                    ),
                ),
            )
        )
    )

    print(
        s.leafSimilar(
            TreeNode(1,
                TreeNode(2),
                TreeNode(3),
            ),
            TreeNode(1,
                TreeNode(3),
                TreeNode(2),
            )
        )
    )

    print(
        s.leafSimilar(
            TreeNode(1, TreeNode(2)),
            TreeNode(2, TreeNode(2)),
        )
    )
