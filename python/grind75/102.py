# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if root:
            queue.append(root)
        ret_val = []

        while queue:
            num_sibling = len(queue)
            siblings: List[int] = []
            for _ in range(num_sibling):
                child = queue.popleft()
                siblings.append(child.val)

                if child.left:
                    queue.append(child.left)
                if child.right:
                    queue.append(child.right)

            ret_val.append(siblings)

        return ret_val


if __name__ == "__main__":

    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    solution = Solution()
    print(solution.levelOrder(None))
