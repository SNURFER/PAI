# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    pre_val: int = -sys.maxsize
    is_valid: bool = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder(root)
        return self.is_valid

    def inorder(self, node: TreeNode):
        if node is None:
            return

        self.inorder(node.left)

        if self.pre_val >= node.val:
            self.is_valid = False
        self.pre_val = node.val

        self.inorder(node.right)


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    node3 = TreeNode(2)
    node4 = TreeNode(10)
    node5 = TreeNode(14)

    node2.left = node1
    node2.right = node4
    node4.left = node3
    node4.right = node5

    solution = Solution()
    print(solution.isValidBST(node2))
