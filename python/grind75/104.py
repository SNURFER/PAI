
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recur_func(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = recur_func(node.left)
            right = recur_func(node.right)

            return max(left, right) + 1

        return recur_func(root)


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    node1.left = node2
    node2.left = node3
    node3.left = node4

    solution = Solution()
    print(solution.maxDepth(node1))
