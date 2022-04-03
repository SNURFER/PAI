from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # don't need to index of value, so it is ok to sort
        nums.sort()
        ret_val = []

        for i in range(len(nums) - 2):
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    if not [nums[i], nums[left], nums[right]] in ret_val:
                        ret_val.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1

        return ret_val


if __name__ == "__main__":
    # nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0, 0, 0, 0]
    nums = [-2,0,1,1,2]
    solution = Solution()
    print(solution.threeSum(nums))
