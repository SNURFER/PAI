from typing import List


class Solution(object):
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x)
        return sum(nums[::2])
        # nums.sort(key=lambda x: -x)
        # output: int = 0
        # for i in range(len(nums)):
        #     if i % 2 == 1:
        #         output += nums[i]
        # return output


if __name__ == "__main__":
    solution = Solution()

    num_arr = [1, 4, 3, 2]

    print(solution.arrayPairSum(num_arr))


