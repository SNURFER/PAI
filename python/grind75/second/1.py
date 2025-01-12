import collections
from typing import List



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans: List[int] = []
        cal_dic = {}

        for idx, val in enumerate(nums):
            need_val = target - val
            if need_val in cal_dic:
                ans.append(idx)
                ans.append(cal_dic[need_val])
                break
            cal_dic[val] = idx

        return ans


if __name__ == "__main__":
    nums = [2, 7, 11, 16]
    target = 27

    solution = Solution()
    print(solution.twoSum(nums, target))
