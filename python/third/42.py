from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        left_max, right_max = 0, 0
        trap_water = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                trap_water += left_max - height[left]
                left += 1
            else:
                trap_water += right_max - height[right]
                right -= 1

        return trap_water


if __name__ == "__main__":
    height = [4, 2, 0, 3, 2, 5]
    solution = Solution()
    print(solution.trap(height))
