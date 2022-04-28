from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(left: int, right: int) -> int:
            if left <= right:
                # be careful. overflow
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    return bs(mid + 1, right)
                elif nums[mid] > target:
                    return bs(left, mid - 1)
                else:
                    return mid

            return -1

        return bs(0, len(nums) - 1)


if __name__ == "__main__":
    # nums = [-1, 0, 3, 5, 9, 12]
    # target = 9
    nums = [5]
    target = 5
    solution = Solution()
    print(solution.search(nums, target))
