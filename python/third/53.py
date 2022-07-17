import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize
        prev_sum = 0

        for num in nums:
            prev_sum = max(prev_sum + num, num)
            max_sum = max(max_sum, prev_sum)

        return max_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [-2]
    solution = Solution()
    print(solution.maxSubArray(nums))
