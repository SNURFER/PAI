# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        self.bstToGst(root.right)
        self.sum += root.val
        root.val = self.sum
        self.bstToGst(root.left)

        return root


if __name__ == "__main__":
    node4 = TreeNode(5)
    node5 = TreeNode(9)
    node2 = TreeNode(7, node4, node5)
    node6 = TreeNode(15)
    node7 = TreeNode(21)
    node3 = TreeNode(20, node6, node7)
    node1 = TreeNode(10, node2, node3)

    solution = Solution()
    solution.bstToGst(node1)

