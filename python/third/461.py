class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xy_xor = x ^ y
        cnt_diff = 0

        while xy_xor > 0:
            cnt_diff += xy_xor % 2
            xy_xor = xy_xor // 2

        return cnt_diff


if __name__ == "__main__":
    x = 1
    y = 4
    solution = Solution()
    print(solution.hammingDistance(x, y))
