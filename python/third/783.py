# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    min_diff = sys.maxsize
    prev_num = -sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node: Optional[TreeNode]):
            if not node:
                return

            inorder(node.left)
            self.min_diff = min(self.min_diff, node.val - self.prev_num)
            self.prev_num = node.val
            inorder(node.right)

        inorder(root)
        return self.min_diff


if __name__ == "__main__":
    # root = [90, 69, null, 49, 89, null, 52]
    node1 = TreeNode(90)
    node2 = TreeNode(69)
    node3 = TreeNode(49)
    node4 = TreeNode(89)
    node5 = TreeNode(52)

    node1.left = node2
    node2.left = node3
    node2.right = node4
    node3.right = node5

    solution = Solution()
    print(solution.minDiffInBST(node1))

