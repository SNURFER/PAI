import collections
import heapq
import sys
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # init graph
        graph = collections.defaultdict(list)
        for s, e, t in times:
            graph[s].append((e, t))

        dist = collections.defaultdict(int)

        q = [(0, k)]
        while q:
            time, node = heapq.heappop(q)

            if node not in dist:
                dist[node] = time
                for e, t in graph[node]:
                    accum = time + t
                    heapq.heappush(q, (accum, e))

        if len(dist) < n:
            return -1

        max_val = -sys.maxsize
        for key in dist:
            max_val = max(max_val, dist[key])

        return max_val


if __name__ == "__main__":
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    solution = Solution()
    print(solution.networkDelayTime(times, n, k))
