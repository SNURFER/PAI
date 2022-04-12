# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest: int = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.longest = max(self.longest, left + right)

            return max(left, right)

        dfs(root)

        return self.longest


if __name__ == "__main__":
    # root = [5, 4, 5, 1, 1, 5]
    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(5)
    node4 = TreeNode(1)
    node5 = TreeNode(1)
    node6 = TreeNode(5)

    node1.left  = node2
    node1.right = node3
    node2.left  = node4
    node2.right = node5
    node3.right = node6

    solution = Solution()
    print(solution.longestUnivaluePath(node1))
