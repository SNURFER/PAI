# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if (left - right) ** 2 > 1:
                self.balanced = False

            return max(left, right) + 1

        dfs(root)
        return self.balanced


if __name__ == "__main__":
    # root = [3, 9, 20, null, null, 15, 7]
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node6 = TreeNode(10)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    node5.right = node6

    solution = Solution()
    print(solution.isBalanced(node1))
