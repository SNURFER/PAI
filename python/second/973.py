import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ret_val = []
        distance_list = []

        for point in points:
            heapq.heappush(distance_list, [point[0] * point[0] + point[1] * point[1], point])

        for _ in range(k):
            ret_val.append(heapq.heappop(distance_list)[1])

        return ret_val


if __name__ == "__main__":
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    # points = [[1, 3], [-2, 2]]
    # k = 1

    solution = Solution()
    print(solution.kClosest(points, k))
