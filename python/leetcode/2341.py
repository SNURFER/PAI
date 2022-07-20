import collections
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        num_cnt = collections.Counter(nums)
        pair_cnt = 0
        non_pair_cnt = 0
        for key in num_cnt:

            pair_cnt += num_cnt[key] // 2
            non_pair_cnt += num_cnt[key] % 2

        return [pair_cnt, non_pair_cnt]


if __name__ == "__main__":
    nums = [1, 3, 2, 1, 3, 2, 2]
    solution = Solution()
    print(solution.numberOfPairs(nums))

