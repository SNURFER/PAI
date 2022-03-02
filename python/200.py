from typing import List


class Solution:
    def dfs(self, row_idx: int, column_idx: int, grid: List[List[str]], visit: List[List[str]]):
        # escape condition
        if row_idx < 0 \
                or row_idx >= len(grid) \
                or column_idx < 0 \
                or column_idx >= len(grid[0]) \
                or grid[row_idx][column_idx] == '0':
                # or visit[row_idx][column_idx] == True:
            return

        grid[row_idx][column_idx] = '0'
        # visit[row_idx][column_idx] = True

        self.dfs(row_idx + 1, column_idx, grid, visit)
        self.dfs(row_idx - 1, column_idx, grid, visit)
        self.dfs(row_idx, column_idx + 1, grid, visit)
        self.dfs(row_idx, column_idx - 1, grid, visit)

    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        row = len(grid)
        column = len(grid[0])
        visit: List[List[bool]] = [[False] * column] * row

        for i in range(row):
            for j in range(column):
                # if not visit[i][j]:
                if grid[i][j] == '1':
                    self.dfs(i, j, grid, visit)
                    counter += 1
                    # visit[i][j] = True

        return counter


if __name__ == "__main__":
    solution = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "0", "1", "0"]
    ]

    print(solution.numIslands(grid))
