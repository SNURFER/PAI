# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        pivot = preorder.pop(0)
        pivot_idx = inorder.index(pivot)

        node = TreeNode(pivot)
        node.left = self.buildTree(preorder, inorder[:pivot_idx])
        node.right = self.buildTree(preorder, inorder[pivot_idx + 1:])

        return node


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    solution = Solution()
    ret_node = solution.buildTree(preorder, inorder)
    print(ret_node)

