import collections
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = collections.defaultdict(lambda: -1)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        def recurFun(n: int) -> int:
            if n < 2 or dp[n] != -1:
                return dp[n]

            dp[n] = max(recurFun(n - 2) + nums[n], recurFun(n - 1))
            return dp[n]

        return recurFun(len(nums) - 1)

        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        #
        # return dp[len(nums) - 1]


if __name__ == "__main__":
    # nums = [2, 7, 9, 3, 1]
    nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # nums = [0]
    solution = Solution()
    print(solution.rob(nums))