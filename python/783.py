# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    min_diff: int = sys.maxsize
    prev: int = -sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inOrderBST(root: Optional[TreeNode]):
            if root is None:
                return

            inOrderBST(root.left)
            self.min_diff = min(self.min_diff, root.val - self.prev)
            self.prev = root.val
            inOrderBST(root.right)

        inOrderBST(root)

        return self.min_diff


if __name__ == "__main__":

    node4 = TreeNode(5)
    node5 = TreeNode(9)
    node2 = TreeNode(7, node4, node5)
    node6 = TreeNode(15)
    node7 = TreeNode(21)
    node3 = TreeNode(20, node6, node7)
    node1 = TreeNode(10, node2, node3)

    solution = Solution()
    print(solution.minDiffInBST(node1))
