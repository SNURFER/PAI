import collections


class Solution:
    dp = collections.defaultdict(lambda: -1)

    def __init__(self):
        self.dp[0] = 0
        self.dp[1] = 1

    def fib(self, n: int) -> int:
        if self.dp[n] != -1:
            return self.dp[n]

        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.dp[n]


if __name__ == "__main__":
    solution = Solution()
    print(solution.fib(100))
