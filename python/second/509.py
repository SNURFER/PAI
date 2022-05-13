import collections


class Solution:
    dp = collections.defaultdict(lambda: -1)
    dp[0] = 0
    dp[1] = 1
    def fib(self, n: int) -> int:
        if self.dp[n] == -1:
            self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]


if __name__ == "__main__":
    solution = Solution()
    print(solution.fib(10))
