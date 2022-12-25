from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        height = len(image)
        width = len(image[0])
        visit = [[False] * width for _ in range(height)]
        target_color = image[sr][sc]
        image[sr][sc] = color

        def dfs(row: int, col: int, image: List[List[int]], visit: List[List[int]]):
            if 0 <= col + 1 < width and visit[row][col + 1] is False and image[row][col + 1] is target_color:
                visit[row][col + 1] = True
                image[row][col + 1] = color
                dfs(row, col + 1, image, visit)
            if 0 <= col - 1 < width and visit[row][col - 1] is False and image[row][col - 1] is target_color:
                visit[row][col - 1] = True
                image[row][col - 1] = color
                dfs(row, col - 1, image, visit)
            if 0 <= row + 1 < height and visit[row + 1][col] is False and image[row + 1][col] is target_color:
                visit[row + 1][col] = True
                image[row + 1][col] = color
                dfs(row + 1, col, image, visit)
            if 0 <= row - 1 < width and visit[row - 1][col] is False and image[row - 1][col] is target_color:
                visit[row - 1][col] = True
                image[row - 1][col] = color
                dfs(row - 1, col, image, visit)

        dfs(sr, sc, image, visit)

        return image


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    solution = Solution()
    print(solution.floodFill(image, sr, sc, color))