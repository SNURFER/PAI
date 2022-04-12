# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum_max: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def recurTraverse(node: Optional[TreeNode]) -> int:
            if not node:
                return -1

            left_max = recurTraverse(node.left)
            right_max = recurTraverse(node.right)

            self.sum_max = max(left_max + right_max + 2, self.sum_max)
            return max(left_max + 1, right_max + 1)

        recurTraverse(root)

        return self.sum_max


if __name__ == "__main__":
    # root = [3, 9, 20, null, null, 15, 7]

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    solution = Solution()
    print(solution.diameterOfBinaryTree(node1))
