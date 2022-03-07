from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []

        for i in range(0, numRows):
            rowList = [1] * (i + 1)
            for j in range(1, int(i / 2) + 1):
                rowList[j] = output[i - 1][j - 1] + output[i - 1][j]
                rowList[i - j] = rowList[j]
            output.append(rowList[:])

        return output


if __name__ == "__main__":
    solution = Solution()
    print(solution.generate(5))
