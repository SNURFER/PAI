import collections
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = collections.defaultdict(lambda: -1)
        dp[0] = nums[0]
        dp[-1] = 0

        def recur_rob(n: int) -> int:
            if dp[n] != -1:
                return dp[n]
            else:
                dp[n] = max(recur_rob(n - 2) + nums[n], recur_rob(n - 1))
                return dp[n]

        return recur_rob(len(nums) - 1)


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    solution = Solution()
    print(solution.rob(nums))
