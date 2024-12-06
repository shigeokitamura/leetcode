# https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def count_paths_from_node(node: Optional[TreeNode], target: int) -> int:
            if not node:
                return 0

            count = 0
            if node.val == target:
                count += 1

            count += count_paths_from_node(node.left, target - node.val)
            count += count_paths_from_node(node.right, target - node.val)

            return count

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            count = count_paths_from_node(node, targetSum)

            count += dfs(node.left)
            count += dfs(node.right)

            return count

        return dfs(root)

if __name__ == "__main__":
    s = Solution()

    print(
        s.pathSum(
            TreeNode(10,
                TreeNode(5,
                    TreeNode(3,
                        TreeNode(3),
                        TreeNode(-2),
                    ),
                    TreeNode(2,
                        None,
                        TreeNode(1),
                    ),
                ),
                TreeNode(-3,
                    None,
                    TreeNode(11),
                ),
            ),
            3,
        )
    ) # 3

    print(
        s.pathSum(
            TreeNode(
                5,
                TreeNode(4,
                    TreeNode(11,
                        TreeNode(7),
                        TreeNode(2),
                    ),
                    None,
                ),
                TreeNode(8,
                    TreeNode(13),
                    TreeNode(4,
                        TreeNode(5),
                        TreeNode(1),
                    ),
                ),
            ),
            22
        )
    ) # 3
