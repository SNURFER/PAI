# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_avg = []
        level_queue = collections.deque([])
        level_queue.append(root)

        while level_queue:
            cal_avg = 0
            node_num = len(level_queue)
            for _ in range(node_num):
                node = level_queue.popleft()
                # ?? no need? why?
                # cal_avg += float("{:.5f}".format(node.val / node_num))

                # also this does not work. this is more save to prevent overflow...
                # cal_avg += node.val / node_num
                cal_avg += node.val

                if node.left:
                    level_queue.append(node.left)
                if node.right:
                    level_queue.append(node.right)
            level_avg.append(cal_avg / node_num)

        return level_avg


if __name__ == "__main__":
    # root = [3, 9, 20, null, null, 15, 7]
    node1 = TreeNode(3)
    node2 = TreeNode(9.28)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    solution = Solution()
    print(solution.averageOfLevels(node1))
