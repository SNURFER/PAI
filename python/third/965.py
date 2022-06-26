# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    isUnival = True
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val_set = set()
        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            val_set.add(node.val)
            if len(val_set) != 1:
                self.isUnival = False
                return

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.isUnival


if __name__ == "__main__":
    # root = [1, 1, 1, 1, 1, null, 1]

    node1 = TreeNode(1)
    node2 = TreeNode(1)
    node3 = TreeNode(1)
    node4 = TreeNode(2)
    node5 = TreeNode(1)
    node6 = TreeNode(1)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node5

    solution = Solution()
    print(solution.isUnivalTree(node1))
