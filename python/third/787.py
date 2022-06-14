import collections
import heapq
import sys
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for s, d, p in flights:
            graph[s].append((d, p))

        Q = [(0, src, 0)]

        ## why not?
        # visit = [False] * n
        visit = [sys.maxsize] * n
        while Q:
            cost, dest, stops = heapq.heappop(Q)
            if dest == dst:
                return cost

            # if stops <= k and not visit[dest]:
            #     visit[dest] = True
            if stops <= k and visit[dest] > stops:
                visit[dest] = stops
                for d, p in graph[dest]:
                    heapq.heappush(Q, (cost + p, d, stops + 1))

        return -1


if __name__ == "__main__":
    # n = 4
    # flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    # src = 0
    # dst = 3
    # k = 1
    # n = 3
    # flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    # src = 0
    # dst = 2
    # k = 0

    n = 5
    flights = [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]
    src = 0
    dst = 2
    k = 2
    solution = Solution()
    print(solution.findCheapestPrice(n, flights, src, dst, k))
