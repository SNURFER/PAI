from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[List[int]] = []
        result = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            print(temp, idx)
            while stack and stack[-1][1] < temp:
                item = stack.pop()
                result[item[0]] = idx - item[0]

            stack.append([idx, temp])

        return result


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    solution = Solution()
    print(solution.dailyTemperatures(temperatures))
