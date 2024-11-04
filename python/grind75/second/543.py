# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest: int = 0
        def bt(node: Optional[TreeNode]) -> int:
            if not node:
                return -1

            left_depth = bt(node.left)
            right_depth = bt(node.right)

            nonlocal longest
            longest = max(left_depth + right_depth + 2, longest)
            return max(left_depth, right_depth) + 1

        bt(root)
        return longest


if __name__ == "__main__":

    node1 = TreeNode(0)
    node2 = TreeNode(0)
    node3 = TreeNode(0)
    node4 = TreeNode(0)
    node5 = TreeNode(0)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    solution = Solution()
    print(solution.diameterOfBinaryTree(node1))
