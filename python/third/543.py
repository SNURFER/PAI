# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def traverse(node: Optional[TreeNode]) -> int:
            if not node:
                return -1

            left: int = traverse(node.left)
            right: int = traverse(node.right)
            self.max_diameter = max(left + right + 2, self.max_diameter)
            return max(left, right) + 1

        traverse(root)
        return self.max_diameter


if __name__ == "__main__":
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    # node6 = TreeNode(15)
    # node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    # node3.left = node6
    # node3.right = node7
    solution = Solution()
    print(solution.diameterOfBinaryTree(node1))

