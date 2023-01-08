class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1 for _ in range(46)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        def recurClimbStairs(n: int) -> int:
            if dp[n] != -1:
                return dp[n]

            dp[n] = recurClimbStairs(n - 1) + recurClimbStairs(n - 2)
            return dp[n]

        return recurClimbStairs(n)


if __name__ == "__main__":
    solution = Solution()
    n = 45
    print(solution.climbStairs(n))
