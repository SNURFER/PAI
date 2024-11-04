from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        if nums[0] > target or nums[-1] < target:
            return -1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m

        return -1


if __name__ == "__main__":
    nums: List[int] = [12]
    solution = Solution()
    print(solution.search(nums, 12))
