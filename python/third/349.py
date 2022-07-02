from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        in_num = set()

        for num in nums1:
            if num in nums2:
                in_num.add(num)

        return list(in_num)


if __name__ == "__main__":
    # nums1 = [4, 9, 5]
    # nums2 = [9, 4, 9, 8, 4]
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    solution = Solution()
    print(solution.intersection(nums1, nums2))
