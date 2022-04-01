import collections


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = collections.defaultdict(int)
        dp[0], dp[1] = 1, 1

        def recurFunc(n: int) -> int:
            if n < 2 or dp[n] != 0:
                return dp[n]
            dp[n] = recurFunc(n - 1) + recurFunc(n - 2)
            return dp[n]

        return recurFunc(n)


if __name__ == "__main__":
    n = 3
    solution = Solution()
    print(solution.climbStairs(0))
    print(solution.climbStairs(1))
    print(solution.climbStairs(2))
    print(solution.climbStairs(n))
    print(solution.climbStairs(38))
