from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        dp: List[int] = [-1] * (n + 1)
        dp[0], dp[1] = 1, 1

        def recur(num: int) -> int:
            if dp[num] != -1:
                return dp[num]

            dp[num] = recur(num - 1) + recur(num - 2)

            return dp[num]

        return recur(n)


if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(5))
