from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = white = 0
        blue = len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            elif nums[white] == 2:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

        for num in nums:
            print(num)



if __name__ == "__main__":
    # nums = [2, 0, 2, 1, 1, 0]
    nums = [2, 0, 1]
    solution = Solution()
    solution.sortColors(nums)
