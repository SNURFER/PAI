import collections
from typing import List


class Solution:
    is_valid = False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        edge_dict = collections.defaultdict(list)
        for edge in edges:
            edge_dict[edge[0]].append(edge[1])
            edge_dict[edge[1]].append(edge[0])

        visit = set()

        def dfs(depart: int):
            if depart == destination:
                self.is_valid = True
                return

            visit.add(depart)
            for dest in edge_dict[depart]:
                if dest not in visit and self.is_valid is False:
                    dfs(dest)

        dfs(source)

        return self.is_valid


if __name__ == "__main__":
    n = 50
    edges = [[19, 27], [10, 43], [6, 45], [36, 23], [38, 26], [14, 8], [31, 11], [11, 49], [32, 33], [17, 10], [18, 38],
     [14, 34], [2, 6], [33, 31], [48, 16], [43, 42], [0, 15], [12, 1], [13, 7], [7, 4], [49, 2], [28, 35], [22, 37],
     [39, 20], [44, 39], [5, 25], [24, 41], [40, 30], [25, 29], [35, 24], [29, 18], [27, 22], [45, 12], [3, 46],
     [20, 40], [37, 32], [16, 19], [15, 44], [9, 47], [4, 5], [8, 9], [23, 48], [30, 3], [47, 17], [41, 0], [1, 21],
     [26, 28], [42, 36], [21, 13]]
    source = 14
    destination = 34
    # n = 6
    # edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    # source = 0
    # destination = 5
    # n = 3
    # edges = [[0, 1], [1, 2], [2, 0]]
    # source = 0
    # destination = 2
    solution = Solution()
    print(solution.validPath(n, edges, source, destination))
