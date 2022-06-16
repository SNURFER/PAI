import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        graph = collections.defaultdict(list)
        cnt = collections.defaultdict(int)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
            cnt[v1] += 1
            cnt[v2] += 1

        height = 0

        while len(cnt) > 2:

            ones = []
            for key in graph:
                if key in cnt and cnt[key] == 1:
                    ones.append(key)

            for key in ones:
                target = graph[key].pop()
                graph[target].remove(key)
                cnt.pop(key)
                cnt[target] -= 1

            height += 1

        return [key for key in cnt]


if __name__ == "__main__":
    # n = 4
    # edges = [[1, 0], [1, 2], [1, 3]]
    # n = 6
    # edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    n = 6
    edges = [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]
    solution = Solution()
    print(solution.findMinHeightTrees(n, edges))
