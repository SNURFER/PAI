# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(1)
    node3 = TreeNode(1)
    node4 = TreeNode(1)
    node5 = TreeNode(1)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node4.right = node5

    solution = Solution()
    print(solution.maxDepth(node1))

