from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(0, len(s) // 2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    solution = Solution()
    solution.reverseString(s)
    print(s)