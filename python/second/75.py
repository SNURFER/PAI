from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        white_idx = red_idx = 0

        blue_idx: int = len(nums) - 1

        idx = red_idx
        while idx <= blue_idx:
            if nums[idx] == 0:
                nums[idx], nums[red_idx] = nums[red_idx], nums[idx]
                red_idx += 1
                white_idx += 1
                idx += 1
            elif nums[idx] == 2:
                nums[idx], nums[blue_idx] = nums[blue_idx], nums[idx]
                blue_idx -= 1
            elif nums[idx] == 1:
                if red_idx <= idx <= blue_idx:
                    idx += 1
                    continue
                else:
                    nums[idx], nums[white_idx] = nums[white_idx], nums[idx]
                    white_idx += 1
                    idx += 1


        print(nums)


if __name__ == "__main__":
    # nums = [2, 0, 2, 1, 1, 0]
    # nums = [2, 1]
    # nums = [1, 2]
    # nums = [2, 0, 1]
    solution = Solution()
    nums = [1, 2]
    solution.sortColors(nums)
    nums = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums)
    nums = [2, 1]
    solution.sortColors(nums)
    nums = [2, 0, 1]
    solution.sortColors(nums)
    nums = [1, 2, 0]
    solution.sortColors(nums)
    # nums = [2, 0, 2, 1, 1, 0]
    # solution.sortColors(nums)

