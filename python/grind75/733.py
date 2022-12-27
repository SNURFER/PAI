from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        height = len(image)
        width = len(image[0])
        visit = [[False] * width for _ in range(height)]
        target_color = image[sr][sc]

        def dfs(row: int, col: int):
            if not (0 <= row < height) or not (0 <= col < width):
                return

            if visit[row][col] is True:
                return

            if image[row][col] is target_color:
                visit[row][col] = True
                image[row][col] = color
                dfs(row, col + 1)
                dfs(row, col - 1)
                dfs(row + 1, col)
                dfs(row - 1, col)

        dfs(sr, sc)

        return image


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    solution = Solution()
    print(solution.floodFill(image, sr, sc, color))