# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self, longest=0):
        self.longest = longest

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)

            return max(left, right) + 1

        dfs(root)
        return self.longest


if __name__ == "__main__":
    solution = Solution()
    node2 = TreeNode(9)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node3 = TreeNode(20, node4, node5)
    node1 = TreeNode(3, node2, node3)
    print(solution.diameterOfBinaryTree(node1))
