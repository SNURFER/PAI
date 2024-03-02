from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)


if __name__ == "__main__":
    node2 = TreeNode(9)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node3 = TreeNode(20, node4, node5)
    node1 = TreeNode(3, node2, node3)
    solution = Solution()
    print(solution.maxDepth(node1))
