# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            #devide
            left = dfs(node.left)
            right = dfs(node.right)

            #conquar
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)
            return max(left, right)

        dfs(root)
        return self.result


if __name__ == "__main__":
    node6 = TreeNode(1)
    node7 = TreeNode(1)
    node2 = TreeNode(4, node6, node7)
    node5 = TreeNode(5)
    node3 = TreeNode(5, None, node5)
    node1 = TreeNode(5, node2, node3)

    solution = Solution()
    print(solution.longestUnivaluePath(node1))

