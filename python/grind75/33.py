from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = right + (left - right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left
        ret_val = -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = right + (left - right) // 2
            mid_pivot = (mid + pivot) % len(nums)
            if nums[mid_pivot] > target:
                right = mid - 1
            elif nums[mid_pivot] < target:
                left = mid + 1
            else:
                ret_val = mid_pivot
                break

        return ret_val


if __name__ == "__main__":
    # nums = [4, 5, 6, 7, 0, 1, 2]
    nums = [3, 1]
    target = 3
    solution = Solution()
    print(solution.search(nums, target))
