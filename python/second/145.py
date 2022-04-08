# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def postorderRecur(node: Optional[TreeNode]):
            if node:
                postorderRecur(node.left)
                postorderRecur(node.right)
                result.append(node.val)

        postorderRecur(root)

        return result


if __name__ == "__main__":
    node1 = TreeNode(1)
    node3 = TreeNode(2)
    node6 = TreeNode(3)
    node1.right = node3
    node3.left = node6

    solution = Solution()
    print(solution.postorderTraversal(node1))
