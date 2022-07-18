import collections
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = collections.defaultdict(lambda: -1)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        def recur(num: int) -> int:
            if num < 0:
                return 0

            if dp[num] != -1:
                return dp[num]

            dp[num] = max(recur(num - 2) + nums[num], recur(num - 1))
            return dp[num]

        return recur(len(nums) - 1)


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    solution = Solution()
    print(solution.rob(nums))
