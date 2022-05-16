import collections


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = collections.defaultdict(lambda: -1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        if dp[n] == -1:
            dp[n] = self.climbStairs(n - 3) + 2 * self.climbStairs(n - 2)

        return dp[n]


if __name__ == "__main__":
    n = 3
    solution = Solution()
    print(solution.climbStairs(n))
