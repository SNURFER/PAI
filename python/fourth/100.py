# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        is_same: bool = True

        def recur(tree1: Optional[TreeNode], tree2: Optional[TreeNode]):
            nonlocal is_same
            if tree1 or tree2:
                if not tree1 and tree2:
                    is_same = False
                elif not tree2 and tree1:
                    is_same = False
                elif tree1.val != tree2.val:
                    is_same = False
                else:
                    recur(tree1.left, tree2.left)
                    recur(tree1.right, tree2.right)

        recur(p, q)

        return is_same


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3

    node4 = TreeNode(1)
    node5 = TreeNode(2)
    node6 = TreeNode(3)
    node4.left = node5
    node4.right = node6

    solution = Solution()
    print(solution.isSameTree(node1, node4))
