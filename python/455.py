from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        g_idx = s_idx = 0
        while g_idx < len(g) and s_idx < len(s):
            if g[g_idx] <= s[s_idx]:
                g_idx += 1
                s_idx += 1
            else:
                s_idx += 1

        return g_idx


if __name__ == "__main__":
    g = [1, 2, 3]
    s = [1, 1]
    solution = Solution()
    print(solution.findContentChildren(g, s))