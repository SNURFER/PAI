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

        left: int = self.maxDepth(root.left)
        right: int = self.maxDepth(root.right)

        return max(left, right) + 1


if __name__ == "__main__":

    # root = [3, 9, 20, null, null, 15, 7]
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node6 = TreeNode(15)
    node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node6
    node3.right = node7

    solution = Solution()
    print(solution.maxDepth(node1))

