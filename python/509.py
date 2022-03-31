import collections


class Solution:
    # dp = collections.defaultdict(int)
    # dp[1] = 1

    def fib(self, n: int) -> int:
        x = 0
        y = 1

        for i in range(0, n):
            x, y = y, x + y

        return x

        # if n <= 0:
        #     return 0
        #
        # if self.dp[n] != 0:
        #     return self.dp[n]
        #
        # self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        # return self.dp[n]


if __name__ == "__main__":
    solution = Solution()

    print(solution.fib(0))
    print(solution.fib(1))
    print(solution.fib(2))
    print(solution.fib(3))
    print(solution.fib(4))
    print(solution.fib(5))
