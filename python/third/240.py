from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ret_val = False
        row = 0
        column = len(matrix[0]) - 1
        while 0 <= row < len(matrix) and 0 <= column < len(matrix[0]):
            if matrix[row][column] == target:
                ret_val = True
                break
            elif matrix[row][column] > target:
                column -= 1
            else:
                row += 1

        return ret_val


if __name__ == "__main__":
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 5
    solution = Solution()
    print(solution.searchMatrix(matrix, target))

