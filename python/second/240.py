from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True

        return False


if __name__ == "__main__":

    # matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
    #           [18, 21, 23, 26, 30]]
    # target = 5
    matrix = [[-5]]
    target = -5

    solution = Solution()
    print(solution.searchMatrix(matrix, target))
