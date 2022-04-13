# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1:
                return -1

            if left - right > 1 or right - left > 1:
                return -1

            return max(left, right) + 1

        ret_val = dfs(root)
        if ret_val == -1:
            return False
        return True


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    node3 = TreeNode(2)
    node4 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node2.left = node4

    solution = Solution()
    print(solution.isBalanced(node1))