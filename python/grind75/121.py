import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_earn = 0
        min_val = sys.maxsize
        for price in prices:
            min_val = min(min_val, price)
            cur_earn = max(price - min_val, cur_earn)

        return cur_earn


if __name__ == "__main__":
    # prices = [7, 1, 5, 3, 6, 4]
    prices = [7, 6, 4, 3, 1]

    solution = Solution()
    print(solution.maxProfit(prices))
