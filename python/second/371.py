class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        # TODO... understand correctly...
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        if a > INT_MAX:
            a = ~(a ^ MASK)

        return a


if __name__ == "__main__":
    a = 2
    b = 3
    solution = Solution()
    print(solution.getSum(a, b))
