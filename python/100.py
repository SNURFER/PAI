from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #escape condition
        if not p and not q:
            return True
        elif not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    solution = Solution()
    node2 = TreeNode(3)
    node3 = TreeNode(3)
    node1 = TreeNode(1, node2, node3)

    node5 = TreeNode(2)
    node6 = TreeNode(3)
    node4 = TreeNode(1, node5, node6)
    print(solution.isSameTree(node1, node4))
