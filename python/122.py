from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1)])


if __name__ == "__main__":
    prices = [7, 6, 4, 3, 1]
    solution = Solution()
    print(solution.maxProfit(prices))