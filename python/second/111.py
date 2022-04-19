# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_min = self.minDepth(root.left)
        right_min = self.minDepth(root.right)

        if min(left_min, right_min) == 0:
            return left_min + right_min + 1
        return min(left_min, right_min) + 1


if __name__ == "__main__":
    root = [3, 9, 20, None, None, 15, 7]

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
    print(solution.minDepth(node1))