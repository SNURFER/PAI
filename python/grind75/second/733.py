from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        M = len(image)
        N = len(image[0])
        src_clr: int = image[sr][sc]
        visit = [[-1] * N for _ in range(M)]

        def dfs(image: List[List[int]], m: int, n: int, source_color: int, target_color: int):
            if visit[m][n] == 1 or image[m][n] != source_color:
                return

            visit[m][n] = 1

            if image[m][n] == source_color:
                image[m][n] = target_color

            if 0 <= m + 1 < M:
                dfs(image, m + 1, n, source_color, target_color)
            if 0 <= m - 1 < M:
                dfs(image, m - 1, n, source_color, target_color)
            if 0 <= n + 1 < N:
                dfs(image, m, n + 1, source_color, target_color)
            if 0 <= n - 1 < N:
                dfs(image, m, n - 1, source_color, target_color)

        dfs(image, sr, sc, src_clr, color)
        return image


if __name__ == "__main__":
    # image = [[0, 1, 1], [1, 1, 0], [1, 0, 1]]
    # sr = 1
    # sc = 1
    # color = 2

    image = [[0,0,0],[0,0,0]]
    sr = 0
    sc = 0
    color = 0
    solution = Solution()
    ret_val = solution.floodFill(image, sr, sc, color)
    for i in range(len(ret_val)):
        for j in range(len(ret_val[0])):
            pass
            print(ret_val[i][j])
