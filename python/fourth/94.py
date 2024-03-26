# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    val_arr: List[int] = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder_impl(root)
        return self.val_arr

    def inorder_impl(self, root: Optional[TreeNode]):
        if root is not None:
            self.inorder_impl(root.left)
            self.val_arr.append(root.val)
            self.inorder_impl(root.right)


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(5)
    node5 = TreeNode(9)

    node1.left = node2
    node1.right = node3
    node2.right = node4
    node4.right = node5

    solution = Solution()
    ret_node: List[int] = solution.inorderTraversal(node1)
    print(ret_node)
