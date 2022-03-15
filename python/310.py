import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        leaves = []
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        for key in graph:
            if len(graph[key]) == 1:
                leaves.append(key)

        while n > 2:
            n = n - len(leaves)
            new_leaves = []
            for leaf in leaves:
                #remove leaf related map values
                neighbor = graph[leaf].pop()
                graph.pop(leaf, None)
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return [key for key in graph]


if __name__ == "__main__":
    # n = 6
    # edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]

    # n = 4
    # edges = [[1, 0], [1, 2], [1, 3]]

    n = 6
    edges = [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]

    solution = Solution()
    print(solution.findMinHeightTrees(n, edges))
