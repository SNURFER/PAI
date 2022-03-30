from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]

        major_num_l = self.majorityElement(nums[:len(nums) // 2])
        major_num_r = self.majorityElement(nums[len(nums) // 2:])

        return [major_num_l, major_num_r][nums.count(major_num_r) > len(nums) // 2]


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    solution = Solution()
    print(solution.majorityElement(nums))