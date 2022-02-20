from typing import List


# [TODO]
class Solution(object):
    def trap(self, height: List[int]) -> int:
        stack: List[int] = []
        stored_water: int = 0

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()

                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                stored_water += distance * waters

            stack.append(i)
        return stored_water


if __name__ == "__main__":
    solution = Solution()
    height_list = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    print(solution.trap(height_list))
