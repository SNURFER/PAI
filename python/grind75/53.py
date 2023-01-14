import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = -sys.maxsize
        sum = 0
        for num in nums:
            sum = max(sum + num, num)
            max_sub = max(sum, max_sub)

        return max_sub


if __name__ == "__main__":
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [1]
    nums = [5, 4, -1, 7, 8]
    solution = Solution()
    print(solution.maxSubArray(nums))
