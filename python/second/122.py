from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        if len(prices) < 2:
            return profit

        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]

        return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    print(solution.maxProfit(prices))
