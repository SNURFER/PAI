from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(depth: int, path: List[int]):
            if depth == k:
                result.append(path)
                return

            for i in range(1, n + 1):
                if not path or path[-1] < i:
                    dfs(depth + 1, path + [i])

        dfs(0, [])
        return result


if __name__ == "__main__":
    n = 4
    k = 2
    solution = Solution()
    print(solution.combine(n, k))
