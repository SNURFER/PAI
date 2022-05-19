from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            rest_num = target - nums[i]
            if rest_num in nums and nums.index(rest_num) != i:
                return [i, nums.index(rest_num)]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums, target))
