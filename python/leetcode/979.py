# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        sum_move = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left: int = dfs(node.left)
            right: int = dfs(node.right)

            nonlocal sum_move
            sum_move += abs(left) + abs(right)

            return (left + right + node.val) - 1

        dfs(root)

        return sum_move


if __name__ == "__main__":
    node1 = TreeNode(0)
    node2 = TreeNode(3)
    node3 = TreeNode(0)
    node1.left = node2
    node1.right = node3

    solution = Solution()
    print(solution.distributeCoins(node1))



