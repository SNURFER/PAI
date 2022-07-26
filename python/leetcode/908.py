from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        if nums[0] + k <= nums[-1] - k:
            return nums[-1] - nums[0] - 2 * k
        else:
            return 0


if __name__ == "__main__":
    nums = [1, 3, 6]
    k = 3
    solution = Solution()
    print(solution.smallestRangeI(nums, k))
