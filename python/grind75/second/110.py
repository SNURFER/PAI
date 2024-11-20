# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            if abs(left_depth - right_depth) > 1:
                nonlocal is_balanced
                is_balanced = False

            return max(left_depth + 1, right_depth + 1)

        dfs(root)
        return is_balanced


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
    print(solution.isBalanced(node1))


