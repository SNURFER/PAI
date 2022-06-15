# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        if root1 and root2:
            left = self.mergeTrees(root1.left, root2.left)
            right = self.mergeTrees(root1.right, root2.right)
            node = TreeNode(root1.val + root2.val)
            node.left = left
            node.right = right
            return node
        else:
            return root1 or root2


if __name__ == "__main__":
    # root1 = [1, 3, 2, 5], root2 = [2, 1, 3, null, 4, null, 7]

    node1 = TreeNode(1)
    node2 = TreeNode(3)
    node3 = TreeNode(2)
    node4 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4

    node5 = TreeNode(2)
    node6 = TreeNode(1)
    node7 = TreeNode(3)
    node9 = TreeNode(4)
    node11 = TreeNode(7)
    node5.left = node6
    node5.right = node7
    node6.right = node9
    node7.right = node11

    solution = Solution()
    solution.mergeTrees(node1, node5)
