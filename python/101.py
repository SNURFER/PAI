from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(left: TreeNode, right: TreeNode):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            else:
                return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)


if __name__ == "__main__":
    solution = Solution()

    # sample_node_list = [1,2,2,3,4,4,3]
    # sample_node_list = [1,2,2,None,3,None,3]

    node7 = TreeNode(3)
    node6 = TreeNode(5)
    node5 = TreeNode(4)
    node4 = TreeNode(3)
    node3 = TreeNode(2, node6, node7)
    node2 = TreeNode(2, node4, node5)
    node1 = TreeNode(1, node2, node3)

    print(solution.isSymmetric(node1))
