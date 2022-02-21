from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        min_val = sum(prices)
        cur_profit = 0
        for price in prices:
            if price < min_val:
                min_val = price
            cur_profit = max(cur_profit, price - min_val)
        return cur_profit


if __name__ == "__main__":
    solution = Solution()
    price_arr = [7, 1, 5, 3, 6, 4]

    print(solution.maxProfit(price_arr))
