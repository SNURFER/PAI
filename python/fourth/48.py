from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.swap_horizontal(matrix)


    def transpose(self, matrix: List[List[int]]) -> None:
        n: int = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def swap_horizontal(self, matrix: List[List[int]]):
        n: int = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]


if __name__ == "__main__":
    input = [[1,2,3],[4,5,6],[7,8,9]]
    solution = Solution()
    solution.rotate(input)
    print(input)



