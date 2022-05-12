from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        a: int = self.majorityElement(nums[0:len(nums) // 2])
        b: int = self.majorityElement(nums[len(nums) // 2:])

        return [a, b][0 if len(nums) // 2 < nums.count(a) else 1]


if __name__ == "__main__":
    # nums = [2, 2, 1, 1, 1, 2, 2]
    nums = [6, 5, 5]
    solution = Solution()
    print(solution.majorityElement(nums))
