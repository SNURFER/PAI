from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, column = 0, len(matrix[0]) - 1

        while row < len(matrix) and column >= 0:
            print('matrix : ' + str(matrix[row][column]) + ', target :' + str(target))
            if matrix[row][column] > target:
                column -= 1
            elif matrix[row][column] < target:
                row += 1
            else:
                return True

        return False


if __name__ == "__main__":

    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 5
    solution = Solution()
    print(solution.searchMatrix(matrix, target))
