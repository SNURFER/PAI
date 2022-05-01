import collections
from typing import List, Set


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()

        nums1.sort()
        nums2.sort()

        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i, j = i + 1, j + 1

        return list(result)


if __name__ == "__main__":

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]

    solution = Solution()
    print(solution.intersection(nums1, nums2))
