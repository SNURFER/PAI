from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret_val = 0
        for num in nums:
            ret_val ^= num

        return ret_val


if __name__ == "__main__":
    # nums = [4, 1, 2, 1, 2]
    nums = [1]
    solution = Solution()
    print(solution.singleNumber(nums))