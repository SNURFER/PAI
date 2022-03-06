from typing import List


class Solution:
    def countBits(self, n:int) -> List[int]:
        if n == 0:
            return [0]

        dp: List[int] = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        output = []

        def recurCountBits(n: int) -> int:
            if dp[n] != -1:
                return dp[n]
            else:
                dp[n] = recurCountBits(int(n / 2)) + (n % 2)
                return dp[n]

        for i in range(n + 1):
            output.append(recurCountBits(i))

        return output


if __name__ == "__main__":
    solution = Solution()
    input = 0

    print(solution.countBits(input))
