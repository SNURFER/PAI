from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        node: TreeNode
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node
        else:
            return t1 or t2


if __name__ == "__main__":
    node4 = TreeNode(5)
    node2 = TreeNode(3, node4, None)
    node3 = TreeNode(2)
    node1 = TreeNode(1, node2, node3)

    node10 = TreeNode(7)
    node7 = TreeNode(3, None, node10)
    node9 = TreeNode(4)
    node6 = TreeNode(1, None, node9)
    node5 = TreeNode(2, node6, node7)

    solution = Solution()
    solution.mergeTrees(node1, node5)
