from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        num = len(nums)
        r, w, b = 0, 0, num - 1

        def recurSort(r_idx: int, w_idx: int, b_idx: int) -> None:
            while w_idx <= b_idx:
                # if red
                if nums[w_idx] == 0:
                    nums[w_idx], nums[r_idx] = nums[r_idx], nums[w_idx]
                    r_idx += 1
                # if blue
                elif nums[w_idx] == 2:
                    nums[w_idx], nums[b_idx] = nums[b_idx], nums[w_idx]
                    b_idx -= 1
                    recurSort(r_idx, w_idx, b_idx)

                w_idx += 1
        recurSort(r, w, b)


if __name__ == "__main__":
    # nums = [2, 0, 2, 1, 1, 0]
    nums = [2, 0, 1]
    solution = Solution()
    solution.sortColors(nums)
    print(nums)

