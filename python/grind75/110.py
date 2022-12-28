from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        is_balance = True

        def recurBST(node: Optional[TreeNode]) -> int:
            nonlocal is_balance
            if node is None:
                return -1

            l_depth = recurBST(node.left)
            r_depth = recurBST(node.right)

            if abs(l_depth - r_depth) > 1:
                is_balance = False

            return max(l_depth + 1, r_depth + 1)

        recurBST(root)
        return is_balance


if __name__ == "__main__":
    node1 = TreeNode(6)
    node2 = TreeNode(2)
    node3 = TreeNode(8)
    node4 = TreeNode(0)
    node5 = TreeNode(4)
    node6 = TreeNode(7)
    node7 = TreeNode(9)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    solution = Solution()
    print(solution.isBalanced(node1))
