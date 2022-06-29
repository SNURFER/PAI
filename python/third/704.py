from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left: int, right: int) -> int:
            if left > right:
                return -1

            mid = left + (right - left) // 2
            if nums[mid] > target:
                return binary_search(left, mid - 1)
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            else:
                return mid

        return binary_search(0, len(nums) - 1)


if __name__ == "__main__":
    nums = [5]
    target = 5
    # nums = [-1, 0, 3, 5, 9, 12]
    # target = 2
    solution = Solution()
    print(solution.search(nums, target))
