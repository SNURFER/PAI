from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x: -x)
        return nums[k - 1]


if __name__ == "__main__":
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    solution = Solution()
    print(solution.findKthLargest(nums, k))
