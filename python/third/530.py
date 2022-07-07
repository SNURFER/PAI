# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev = -sys.maxsize
    min_diff = sys.maxsize
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def inorder(node: Optional[TreeNode]):
            if not node:
                return

            inorder(node.left)

            # inorder visit and do something
            self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val

            inorder(node.right)
        inorder(root)
        return self.min_diff


if __name__ == "__main__":
    # root = [4, 2, 6, 1, 3]
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(6)
    node4 = TreeNode(1)
    node5 = TreeNode(3)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    solution = Solution()
    print(solution.getMinimumDifference(node1))
