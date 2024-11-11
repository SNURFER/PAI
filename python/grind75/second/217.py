from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            seen.add(num)

        return len(seen) != len(nums)


if __name__ == "__main__":
    nums = [1, 2, 3, 3]
    solution = Solution()
    print(solution.containsDuplicate(nums))