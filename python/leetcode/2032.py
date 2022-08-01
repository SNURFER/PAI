import collections
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        num_counter = collections.defaultdict(int)

        for num in set(nums1):
            num_counter[num] += 1
        for num in set(nums2):
            num_counter[num] += 1
        for num in set(nums3):
            num_counter[num] += 1

        ret_val = []
        for key in num_counter:
            if num_counter[key] > 1:
                ret_val.append(key)

        return ret_val


if __name__ == "__main__":
    nums1 = [1, 1, 3, 2]
    nums2 = [2, 3]
    nums3 = [3]
    solution = Solution()
    print(solution.twoOutOfThree(nums1, nums2, nums3))
