# Definition for a Node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ret: TreeNode = TreeNode()

    def increasingBST(self, root: TreeNode) -> TreeNode:
        head = self.ret

        def inorder(node: TreeNode):
            if not node:
                return None

            inorder(node.left)
            new_node = TreeNode(node.val)
            self.ret.right = new_node
            self.ret = self.ret.right
            inorder(node.right)

        inorder(root)

        return head.right


if __name__ == "__main__":
    node4 = TreeNode(5)
    node5 = TreeNode(9)
    node2 = TreeNode(7, node4, node5)
    node6 = TreeNode(15)
    node7 = TreeNode(21)
    node3 = TreeNode(20, node6, node7)
    node1 = TreeNode(10, node2, node3)

    solution = Solution()
    solution.increasingBST(node1)
