from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:k]


if __name__ == "__main__":
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    solution = Solution()
    print(solution.kClosest(points, k))

