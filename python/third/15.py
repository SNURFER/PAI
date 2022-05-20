from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(0, len(nums)):
            num_i = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if num_i + nums[j] + nums[k] > 0:
                    k -= 1
                elif num_i + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    if [num_i, nums[j], nums[k]] not in result:
                        result.append([num_i, nums[j], nums[k]])
                    k -= 1
                    j += 1

        return result


if __name__ == "__main__":
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [0,0,0,0]
    solution = Solution()
    print(solution.threeSum(nums))

