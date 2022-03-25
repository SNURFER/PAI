import bisect
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersected_num = set({})
        nums2.sort()
        for num in nums1:
            idx = bisect.bisect_left(nums2, num)
            if 0 <= idx < len(nums2) and nums2[idx] == num:
                intersected_num.add(num)

        return list(intersected_num)


if __name__ == "__main__":
    solution = Solution()
    # nums1 = [4, 9, 5]
    # nums2 = [9, 4, 9, 8, 4]
    nums1 = [1, 2]
    nums2 = [1, 1]
    print(solution.intersection(nums1, nums2))