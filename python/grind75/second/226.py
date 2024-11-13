# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return

            right_node = dfs(node.right)
            left_node = dfs(node.left)
            node.right = left_node
            node.left = right_node
            return node

        return dfs(root)


if __name__ == "__main__":

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(6)
    node6 = TreeNode(8)
    node7 = TreeNode(9)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    solution = Solution()
    ret_node = solution.invertTree(node1)

    stack = [ret_node]

    while stack:
        cur_node = stack.pop()
        print(cur_node.val)
        if cur_node.left:
            stack.append(cur_node.left)
        if cur_node.right:
            stack.append(cur_node.right)



