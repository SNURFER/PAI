
# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret_val = []
        def dfs(node: Node):


if __name__ == "__main__":
    solution = Solution()
    solution.postorder()