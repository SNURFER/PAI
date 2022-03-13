# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])

        while queue:
            sub_root = queue.popleft()

            sub_root.left, sub_root.right = sub_root.right, sub_root.left

            if sub_root.left:
                queue.append(sub_root.left)
            if sub_root.right:
                queue.append(sub_root.right)

        return root


if __name__ == "__main__":
    node6 = TreeNode(1)
    node7 = TreeNode(3)
    node2 = TreeNode(2, node6, node7)
    node5 = TreeNode(6)
    node8 = TreeNode(9)
    node3 = TreeNode(7, node5, node8)
    node1 = TreeNode(4, node2, node3)

    solution = Solution()
    solution.invertTree(node1)
