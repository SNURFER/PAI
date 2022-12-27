# need to solve again


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurSearch(node: TreeNode) -> TreeNode:
            if not node:
                return None

            if node.val > p.val and node.val > q.val:
                return recurSearch(node.left)

            if node.val < q.val and node.val < p.val:
                return recurSearch(node.right)

            return node

        return recurSearch(root)


if __name__ == "__main__":
    node1 = TreeNode(6)
    node2 = TreeNode(2)
    node3 = TreeNode(8)
    node4 = TreeNode(0)
    node5 = TreeNode(4)
    node6 = TreeNode(7)
    node7 = TreeNode(9)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    solution = Solution()
    ret_val = solution.lowestCommonAncestor(node1, node2, node3)
    print(ret_val.val)
