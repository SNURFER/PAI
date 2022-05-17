from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        # # should keep O(1) memory so this does not work
        # return s[::-1]
        for i in range(0, len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]

        print(s)


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]

    solution = Solution()
    solution.reverseString(s)
