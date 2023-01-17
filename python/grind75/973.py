import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sorted_points = []
        ret_points = []
        for x, y in points:
            heapq.heappush(sorted_points, (x * x + y * y, [x, y]))

        for _ in range(k):
            ret_points.append(heapq.heappop(sorted_points)[-1])
        return ret_points


if __name__ == "__main__":
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    solution = Solution()
    print(solution.kClosest(points, k))
