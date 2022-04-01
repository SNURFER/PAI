import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_cur = 0
        max_sum = -sys.maxsize

        for num in nums:
            max_cur = max(max_cur + num, num)
            max_sum = max(max_sum, max_cur)

        return max_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    print(solution.maxSubArray(nums))