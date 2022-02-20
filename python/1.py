import collections
from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = collections.defaultdict(int)
        for i, n in enumerate(nums):
            num_map[n] = i

        num1: int
        num2: int
        for i, n in enumerate(nums):
            # if num_map[target - n] and num_map[target - n] != i:
            if target - n in num_map and num_map[target - n] != i:
                num1 = i
                num2 = num_map[target - n]
                break

        return [num1, num2]


if __name__ == "__main__":
    solution = Solution()

    # num_arr = [2, 7, 11, 15]
    # tar = 9

    num_arr = [2, 5, 5, 11]
    tar = 10
    print(solution.twoSum(num_arr, tar))
