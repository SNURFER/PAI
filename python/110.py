from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1 or (left - right) * (left - right) > 1:
                return -1
            else:
                return max(left, right) + 1
        return dfs(root) != -1


if __name__ == "__main__":
    node9 = TreeNode(4)
    node8 = TreeNode(4)
    node5 = TreeNode(3)
    node4 = TreeNode(3, node8, node9)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(2)
    node1 = TreeNode(1, node2, node3)

    solution = Solution()
    print(solution.isBalanced(node1))
