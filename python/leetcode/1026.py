# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_v = -sys.maxsize

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def post_order(node: Optional[TreeNode]) -> tuple[int, int]:
            # return val is min, max.
            # node.val >= 0, so leaf returns -1, -1
            if not node:
                return -1, -1

            min_left, max_left = post_order(node.left)
            min_right, max_right = post_order(node.right)

            min_cur = node.val
            max_cur = node.val
            # left is not none
            if min_left >= 0:
                self.max_v = max(abs(node.val - min_left), abs(node.val - max_left), self.max_v)
                min_cur = min(min_left, node.val)
                max_cur = max(max_left, node.val)

            # right is not none
            if min_right >= 0:
                self.max_v = max(abs(node.val - min_right), abs(node.val - max_right), self.max_v)
                min_cur = min(min_right, min_cur)
                max_cur = max(max_right, max_cur)

            print(min_cur, max_cur)
            return min_cur, max_cur

        post_order(root)

        return self.max_v


if __name__ == "__main__":
    # root = [1, null, 2, null, 0, 3]

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(0)
    node4 = TreeNode(3)

    node1.right = node2
    node2.right = node3
    node3.left = node4

    solution = Solution()
    print(solution.maxAncestorDiff(node1))
