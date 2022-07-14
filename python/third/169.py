import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # num_cnt = collections.Counter(nums)
        # return num_cnt.most_common(1)[0][0]
        num_cnt = collections.defaultdict(int)

        for num in nums:
            if num_cnt[num] == 0:
                num_cnt[num] = nums.count(num)
                if len(nums) == 1:
                    return num
            else:
                if num_cnt[num] > len(nums) // 2:
                    return num


if __name__ == "__main__":
    # nums = [2, 2, 1, 1, 1, 2, 2]
    nums = [2]
    solution = Solution()
    print(solution.majorityElement(nums))

