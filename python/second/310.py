import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]

        node_dict = collections.defaultdict(list)
        for edge in edges:
            node_dict[edge[0]].append(edge[1])
            node_dict[edge[1]].append(edge[0])

        leaves = []
        for key in node_dict:
            if len(node_dict[key]) == 1:
                leaves.append(key)

        while n > 2:
            n -= len(leaves)

            new_leaves = []
            for leaf in leaves:
                neighbor = node_dict[leaf].pop()
                node_dict[neighbor].remove(leaf)

                if len(node_dict[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves


if __name__ == "__main__":
    # n = 6
    # edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    n = 2
    edges = [[0, 1]]

    solution = Solution()
    print(solution.findMinHeightTrees(n, edges))

