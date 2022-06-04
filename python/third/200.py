from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_inner_bound(i: int, j: int):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return False
            return True

        def dfs(i: int, j: int):
            if not is_inner_bound(i, j) or grid[i][j] == "0":
                return

            grid[i][j] = "0"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        island_cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island_cnt += 1
                    dfs(i, j)

        return island_cnt


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    solution = Solution()
    print(solution.numIslands(grid))
