from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = [[False] * len(grid[0]) for i in range(len(grid))]
        counter = 0

        # this is wrong! https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
        # visit = [[False] * len(grid[0])] * len(grid)

        def dfs(x: int, y: int):
            visit[x][y] = True
            if grid[x][y] == 0:
                return

            if x - 1 >= 0 and grid[x - 1][y] == '1' and not visit[x - 1][y]:
                dfs(x - 1, y)
            if x + 1 < len(grid) and grid[x + 1][y] == '1' and not visit[x + 1][y]:
                dfs(x + 1, y)
            if y - 1 >= 0 and grid[x][y - 1] == '1' and not visit[x][y - 1]:
                dfs(x, y - 1)
            if y + 1 < len(grid[0]) and grid[x][y + 1] == '1' and not visit[x][y + 1]:
                dfs(x, y + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visit[i][j] and grid[i][j] == '1':
                    counter += 1
                    dfs(i, j)

        return counter


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    solution = Solution()
    print(solution.numIslands(grid))