from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_multi = []
        r_multi = []
        pre_val_l = 1
        pre_val_r = 1

        result = []

        for i in range(0, len(nums) - 1):
            pre_val_l *= nums[i]
            l_multi.append(pre_val_l)

        for i in range(len(nums) - 1, 0, -1):
            pre_val_r *= nums[i]
            r_multi.append(pre_val_r)

        r_multi.reverse()

        l_multi = [1] + l_multi
        r_multi = r_multi + [1]

        for i in range(0, len(nums)):
            result.append((l_multi[i] * r_multi[i]))

        return result


if __name__ == "__main__":
    # nums = [-1, 1, 0, -3, 3]
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.productExceptSelf(nums))
