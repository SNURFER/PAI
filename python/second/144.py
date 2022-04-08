# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def preorderRecur(node: Optional[TreeNode]):
            if node:
                result.append(node.val)
                preorderRecur(node.left)
                preorderRecur(node.right)

        preorderRecur(root)

        return result


if __name__ == "__main__":
    node1 = TreeNode(1)
    node3 = TreeNode(2)
    node6 = TreeNode(3)
    node1.right = node3
    node3.left = node6

    solution = Solution()
    print(solution.preorderTraversal(node1))
