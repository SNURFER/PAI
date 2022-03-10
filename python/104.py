import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                sub_root = queue.popleft()

                if sub_root.left:
                    queue.append(sub_root.left)
                if sub_root.right:
                    queue.append(sub_root.right)

        return depth


if __name__ == "__main__":
    solution = Solution()
    node2 = TreeNode(9)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node3 = TreeNode(20, node4, node5)
    node1 = TreeNode(3, node2, node3)
    print(solution.maxDepth(node1))
