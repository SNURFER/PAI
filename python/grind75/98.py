# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     is_valid = True
    #
    #     def inorder(node: Optional[TreeNode]) -> int:
    #         if not node:
    #             return
    #
    #         left_val = inorder(node.left)
    #         if left_val >= node.val:
    #             nonlocal is_valid
    #             is_valid = False
    #         right_val = inorder(node.right)
    #
    #         return right_val
    #
    #     inorder(root)
    #     return is_valid

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nums = []

        def inorder(node: Optional[TreeNode]) -> int:
            if not node:
                return

            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        inorder(root)
        return nums == sorted(nums) and len(set(nums)) == len(nums)


if __name__ == "__main__":
    node1 = TreeNode(2)
    node2 = TreeNode(1)
    node3 = TreeNode(3)

    node1.left = node2
    node1.right = node3

    solution = Solution()
    print(solution.isValidBST(node1))


