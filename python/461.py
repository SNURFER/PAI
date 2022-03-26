class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_num = x ^ y
        ones = 0
        while xor_num > 0:
            ones += xor_num % 2
            xor_num = xor_num // 2

        # count is list function
        # return bin(x ^ y).count('1')
        return ones


if __name__ == "__main__":
    x = 1
    y = 4
    solution = Solution()
    print(solution.hammingDistance(x, y))

    mask = 0xF
    print(bin(-5))
    print(bin(-5 & mask))
