# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ret_val = []
        def inorder(node: Optional[TreeNode]):
            if not node:
                return

            inorder(node.left)
            ret_val.append(node.val)
            inorder(node.right)

        inorder(root)
        return ret_val[k - 1]


if __name__ == "__main__":
    root = [3, 1, 4, None, 2]
    k = 1

    node1 = TreeNode(3)
    node2 = TreeNode(1)
    node3 = TreeNode(4)
    node5 = TreeNode(2)

    node1.left = node2
    node1.right = node3
    node2.right = node5

    solution = Solution()
    print(solution.kthSmallest(node1, k))