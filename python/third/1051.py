from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sorted = sorted(heights)
        cnt = 0
        for i, height in enumerate(heights):
            if height is not heights_sorted[i]:
                cnt += 1

        return cnt


if __name__ == "__main__":
    heights = [1, 1, 4, 2, 1, 3]
    solution = Solution()
    print(solution.heightChecker(heights))
