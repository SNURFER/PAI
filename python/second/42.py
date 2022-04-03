from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        left_max = height[left]
        right_max = height[right]

        sum = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                sum += left_max - height[left]
                left += 1
            else:
                sum += right_max - height[right]
                right -= 1

        return sum


if __name__ == "__main__":
    height = [4, 2, 0, 3, 2, 5]
    solution = Solution()
    print(solution.trap(height))