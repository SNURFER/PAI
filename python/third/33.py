from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sorted_num = sorted(nums)
        pivot_idx = sorted_num.index(nums[0])

        def bin_search(left: int, right: int) -> int:
            if left <= right:
                mid = left + (right - left) // 2
                if sorted_num[mid] < target:
                    return bin_search(mid + 1, right)
                elif sorted_num[mid] > target:
                    return bin_search(left, mid - 1)
                else:
                    return mid

            return -1

        search_idx = bin_search(0, len(nums) - 1)
        if search_idx == -1:
            return -1
        return (search_idx - pivot_idx + len(nums)) % len(nums)


if __name__ == "__main__":
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 7
    nums = [1, 3]
    target = 1
    solution = Solution()
    print(solution.search(nums, target))

