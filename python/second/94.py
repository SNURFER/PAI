# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret_val = []

        def inorderRecur(node: Optional[TreeNode]):
            if node is not None:
                inorderRecur(node.left)
                ret_val.append(node.val)
                inorderRecur(node.right)

        inorderRecur(root)

        return ret_val


if __name__ == "__main__":
    node1 = TreeNode(1)
    node3 = TreeNode(2)
    node6 = TreeNode(3)
    node1.right = node3
    node3.left = node6

    solution = Solution()
    print(solution.inorderTraversal(node1))
