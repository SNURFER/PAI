
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter: int = 0

        def recurBinary(node: Optional[TreeNode]) -> int:
            if not node:
                return -1

            left = recurBinary(node.left)
            right = recurBinary(node.right)

            nonlocal max_diameter
            max_diameter = max(max_diameter, left + right + 2)

            return max(left, right) + 1

        recurBinary(root)
        return max_diameter


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(1)
    node3 = TreeNode(1)
    node4 = TreeNode(1)
    node5 = TreeNode(1)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    solution = Solution()
    print(solution.diameterOfBinaryTree(node1))
