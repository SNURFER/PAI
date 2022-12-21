from typing import List
import collections

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = collections.defaultdict(list)
        for idx, num in enumerate(nums):
            num_map[num].append(idx)

        for idx_1, tar_1 in enumerate(nums):
            if len(num_map[target - tar_1]) > 0:
                for idx_2 in num_map[target - tar_1]:
                    if idx_1 is not idx_2:
                        return [idx_1, idx_2]


if __name__ == "__main__":
    # nums = [2, 7, 11, 15]
    nums = [3, 1, 3]
    target = 6
    solution = Solution()
    print(solution.twoSum(nums, target))
