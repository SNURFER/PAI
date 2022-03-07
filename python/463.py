from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    counter += 4
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        counter -= 1
                    if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                        counter -= 1
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        counter -= 1
                    if i + 1 < len(grid) and grid[i + 1][j] == 1:
                        counter -= 1
        return counter


if __name__ == "__main__":
    solution = Solution()
    # grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    grid = [[0,1,1]]
    print(solution.islandPerimeter(grid))
