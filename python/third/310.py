import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        graph = collections.defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        leaves = []
        for v in range(n):
            if len(graph[v]) == 1:
                leaves.append(v)

        while n > 2:
            n -= len(leaves)

            new_leaves = []
            for leaf in leaves:
                target = graph[leaf].pop()
                graph[target].remove(leaf)
                if len(graph[target]) == 1:
                    new_leaves.append(target)

            leaves = new_leaves

        return leaves


if __name__ == "__main__":
    # n = 4
    # edges = [[1, 0], [1, 2], [1, 3]]
    # n = 6
    # edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    n = 6
    edges = [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]
    solution = Solution()
    print(solution.findMinHeightTrees(n, edges))
