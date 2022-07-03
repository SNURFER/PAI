from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ret = 0
        for num in nums:
            ret ^= num

        return ret


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    solution = Solution()
    print(solution.singleNumber(nums))
