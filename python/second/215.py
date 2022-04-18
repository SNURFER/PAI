from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x: -x)
        return nums[k - 1]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    solution = Solution()
    print(solution.findKthLargest(nums, k))