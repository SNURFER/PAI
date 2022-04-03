import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]

        max_profit = 0
        for price in prices:
            if min_val < price:
                max_profit = max(max_profit, price - min_val)
            else:
                min_val = price

        return max_profit


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit(prices))
