from typing import List


class Solution(object):
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        # store index of list
        stack = []
        output = [0] * len(t)

        for idx, num in enumerate(t):
            while stack and t[stack[-1]] < num:
                prev_idx = stack.pop()
                output[prev_idx] = idx - prev_idx

            stack.append(idx)

        return output


if __name__ == "__main__":
    solution = Solution()

    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(solution.dailyTemperatures(T))
