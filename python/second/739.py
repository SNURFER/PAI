from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        temp_stack = []

        for idx, temp in enumerate(temperatures):

            while temp_stack and temp > temperatures[temp_stack[-1]]:
                prev_idx = temp_stack.pop()
                result[prev_idx] = idx - prev_idx

            temp_stack.append(idx)

        return result


if __name__ == "__main__":
    # temperatures = [71, 69, 72, 76, 73]
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    solution = Solution()
    print(solution.dailyTemperatures(temperatures))
