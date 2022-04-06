from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(start: int, visit: [], k: int):
            if k == 0:
                result.append(visit)
                return

            for i in range(start, n):
                dfs(i + 1, visit + [i + 1], k - 1)

        dfs(0, [], k)

        return result


if __name__ == "__main__":
    n = 4
    k = 2
    solution = Solution()
    print(solution.combine(n, k))
