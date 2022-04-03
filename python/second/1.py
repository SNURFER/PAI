from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            sub_num = target - nums[i]
            if sub_num in nums[i + 1:]:
                return [i, nums[i + 1:].index(sub_num) + i + 1]


if __name__ == "__main__":
    # nums = [2, 7, 11, 15]
    # target = 9
    nums = [3, 2, 4]
    target = 6
    solution = Solution()
    print(solution.twoSum(nums, target))