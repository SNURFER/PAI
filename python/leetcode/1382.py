# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_val = []

        def dfs(node: TreeNode):
            if not node:
                return

            dfs(node.left)
            sorted_val.append(node.val)
            dfs(node.right)

        def preorderBST(sorted_val: List[int], node: TreeNode):
            mid_idx = len(sorted_val) // 2

            node.val = sorted_val[mid_idx]
            if len(sorted_val[:mid_idx]) > 0:
                left_node = TreeNode()
                node.left = left_node
                preorderBST(sorted_val[:mid_idx], left_node)
            if len(sorted_val[mid_idx + 1:]) > 0:
                right_node = TreeNode()
                node.right = right_node
                preorderBST(sorted_val[mid_idx + 1:], right_node)

        dfs(root)
        ans_node = TreeNode()
        preorderBST(sorted_val, ans_node)
        return ans_node


if __name__ == "__main__":

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.right = node2
    node2.right = node3
    node3.right = node4
    node4.right = node5

    solution = Solution()
    solution.balanceBST(node1)
