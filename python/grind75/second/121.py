from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - min_val)
            min_val = min(min_val, prices[i])

        return max_profit


if __name__ == "__main__":

    prices = [7, 1, 5, 3, 6, 4]

    solution = Solution()
    print(solution.maxProfit(prices))
