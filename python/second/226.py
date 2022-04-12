# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            node.left, node.right = right, left
            return node

        head = dfs(root)

        return head


if __name__ == "__main__":
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
    result = solution.invertTree(node1)

    print(result)

