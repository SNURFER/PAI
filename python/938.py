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
        def inOrderBST(root: Optional[TreeNode], low: int, high: int):
            if root is None:
                return

            if root.val >= low:
                inOrderBST(root.left, low, high)

            if low <= root.val <= high:
                self.sum += root.val

            if root.val <= high:
                inOrderBST(root.right, low, high)

        inOrderBST(root, low, high)
        return self.sum


if __name__ == "__main__":
    node4 = TreeNode(5)
    node5 = TreeNode(9)
    node2 = TreeNode(7, node4, node5)
    node6 = TreeNode(15)
    node7 = TreeNode(21)
    node3 = TreeNode(20, node6, node7)
    node1 = TreeNode(10, node2, node3)

    solution = Solution()
    print(solution.rangeSumBST(node1, 6, 15))

    print(9+7+15+10)