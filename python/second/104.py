# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([])

        if not root:
            return 0

        queue.append(root)

        depth = 0
        while queue:
            depth += 1

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth


if __name__ == "__main__":
    # root = [3, 9, 20, null, null, 15, 7]

    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node6 = TreeNode(15)
    node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node6
    node3.right = node7

    solution = Solution()
    print(solution.maxDepth(node1))
