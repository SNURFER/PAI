import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(key=lambda x: x)
        dp = [sys.maxsize for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    break
                if dp[i - coin] != sys.maxsize:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] < sys.maxsize else -1


if __name__ == "__main__":
    coins = [5, 2, 1]
    amount = 11
    solution = Solution()
    print(solution.coinChange(coins, amount))
