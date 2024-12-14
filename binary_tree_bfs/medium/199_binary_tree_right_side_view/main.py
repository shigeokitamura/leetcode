# https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=leetcode-75

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if not root:
            return result

        queue = deque([root])

        while queue:
            tmp = deque()
            flag = False # Whether the rightmost node of the current level is added to result

            for node in queue:
                if not flag:
                    result.append(node.val)
                    flag = True

                if node.right:
                    tmp.append(node.right)
                if node.left:
                    tmp.append(node.left)

            queue = tmp
        return result

if __name__ == "__main__":
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    print(s.rightSideView(root)) # [1, 3, 4]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.right = TreeNode(3)
    print(s.rightSideView(root)) # [1, 3, 4, 5]

    root = TreeNode(1)
    root.right = TreeNode(3)
    print(s.rightSideView(root)) # [1, 3]

    root = None
    print(s.rightSideView(root)) # []
