from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_idx = 0
        r_idx = len(nums) - 1

        while l_idx <= r_idx:
            m_idx = l_idx + (r_idx - l_idx) // 2

            if nums[m_idx] > target:
                r_idx = m_idx - 1
            elif nums[m_idx] < target:
                l_idx = m_idx + 1
            else:
                return m_idx

        return -1


    def recur_search(self, nums: List[int], target: int) -> int:
        def recur(left: int, right: int) -> int:
            if left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                    return recur(left, right)
                elif nums[mid] > target:
                    right = mid - 1
                    return recur(left, right)
                else:
                    return mid
            else:
                return -1

        return recur(0, len(nums) - 1)


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    # nums = [5]
    # target = 5
    solution = Solution()
    print(solution.search(nums, target))
    print(solution.recur_search(nums, target))

