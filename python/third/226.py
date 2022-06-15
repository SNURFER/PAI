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
        if not root:
            return root

        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left and node.right:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
            elif not node.left and node.right:
                node.left = node.right
                node.right = None
                queue.append(node.left)
            elif not node.right and node.left:
                node.right = node.left
                node.left = None
                queue.append(node.right)

        return root


if __name__ == "__main__":
    # root = [4, 2, 7, 1, 3, 6, 9]
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    # node3 = TreeNode(7)
    # node4 = TreeNode(1)
    # node5 = TreeNode(3)
    # node6 = TreeNode(6)
    # node7 = TreeNode(9)

    node1.left = node2
    # node1.right = node3
    # node2.left = node4
    # node2.right = node5
    # node3.left = node6
    # node3.right = node7

    solution = Solution()
    solution.invertTree(node1)

