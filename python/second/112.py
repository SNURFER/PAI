# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ret_val = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node: Optional[TreeNode], path: []):
            # is leaf
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    self.ret_val = True
                return

            if node.left:
                dfs(node.left, path + [node.left.val])
            if node.right:
                dfs(node.right, path + [node.right.val])
        dfs(root, [root.val])
        return self.ret_val


if __name__ == "__main__":
    # root = [1, 2, 3]
    targetSum = 5
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3

    solution = Solution()
    print(solution.hasPathSum(node1, targetSum))
