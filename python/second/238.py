import collections
from typing import List

# TODO please...remember
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []

        p = 1
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= p
            p *= nums[i]

        return out


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.productExceptSelf(nums))
