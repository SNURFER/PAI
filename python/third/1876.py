class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(0, len(s) - 2):
            if len(set(s[i: i + 3])) > 2:
                cnt += 1

        return cnt


if __name__ == "__main__":
    s = "aababcabc"
    # s = "xyzzaz"
    solution = Solution()
    print(solution.countGoodSubstrings(s))

