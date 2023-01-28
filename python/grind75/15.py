from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplet = []
        length = len(nums)
        for l in range(length):
            m = l + 1
            r = length - 1

            target = -nums[l]

            while m < r:
                if nums[m] + nums[r] > target:
                    r = r - 1
                elif nums[m] + nums[r] < target:
                    m = m + 1
                else:
                    if [nums[l], nums[m], nums[r]] not in triplet:
                        triplet.append([nums[l], nums[m], nums[r]])
                    m = m + 1
                    r = r - 1

        return triplet


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    print(solution.threeSum(nums))
