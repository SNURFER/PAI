from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = 0
        white = 0
        # T.T len(nums) - 1 does not work
        blue = len(nums)

        while white < blue:
            if nums[white] < 1:
                # means red
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1

            elif nums[white] > 1:
                # means blue
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]

            else:
                # means white
                white += 1


if __name__ == "__main__":
    # nums = [2, 0, 2, 1, 1, 0]
    # nums = [1, 2]
    nums = [2, 0, 1]

    solution = Solution()
    solution.sortColors(nums)

    print(nums)
