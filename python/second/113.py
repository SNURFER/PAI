# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret_val = []
        def dfs(node: Optional[TreeNode], path: List[int]):
            if sum(path) == targetSum and not node.left and not node.right:
                ret_val.append(path)
                return

            if node.left:
                dfs(node.left, path + [node.left.val])
            if node.right:
                dfs(node.right, path + [node.right.val])

        if not root:
            return []
        dfs(root, [root.val])
        return ret_val


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    # node3 = TreeNode(3)

    node1.left = node2
    # node1.right = node3

    solution = Solution()
    print(solution.pathSum(node1, 1))