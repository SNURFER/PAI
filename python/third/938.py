# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum: int = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def preorder(node: Optional[TreeNode]):
            if not node:
                return

            if low <= node.val <= high:
                self.sum += node.val

            if node.val < low:
                preorder(node.right)
            elif node.val > high:
                preorder(node.left)
            else:
                preorder(node.right)
                preorder(node.left)

        preorder(root)

        return self.sum


if __name__ == "__main__":
    # root = [10, 5, 15, 3, 7, null, 18]
    node1 = TreeNode(10)
    node2 = TreeNode(5)
    node3 = TreeNode(15)
    node4 = TreeNode(3)
    node5 = TreeNode(7)
    node6 = TreeNode(18)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6

    low = 7
    high = 15
    solution = Solution()
    print(solution.rangeSumBST(node1, low, high))
