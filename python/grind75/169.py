from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # num_counter = Counter(nums)
        # return num_counter.most_common()[0][0]
        return sorted(nums)[len(nums) // 2]


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    solution = Solution()
    print(solution.majorityElement(nums))
