from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = right + (left - right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        min_idx = left
        nums.sort()

        sorted_left = 0
        sorted_right = len(nums) - 1
        sorted_idx = 0
        while sorted_left <= sorted_right:
            if sorted_left == sorted_right and nums[sorted_left] != target:
                return -1

            mid = sorted_right + (sorted_left - sorted_right) // 2

            if nums[mid] < target:
                sorted_left = mid + 1
            elif nums[mid] > target:
                sorted_right = mid - 1
            else:
                sorted_idx = mid
                break

        if sorted_left <= sorted_right:
            return (min_idx + sorted_idx) % len(nums)
        else:
            return -1


if __name__ == "__main__":
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 3
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 0
    # nums = [1]
    # target = 0
    nums, target = [1, 3], 0

    solution = Solution()
    print(solution.search(nums, target))