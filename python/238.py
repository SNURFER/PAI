from typing import List


class Solution(object):
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
    solution = Solution()

    num_arr = [1, 2, 3, 4]
    print(solution.productExceptSelf(num_arr))

