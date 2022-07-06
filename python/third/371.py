class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFF
        MAX_PLUS = 0x7FFF
        a_bin = bin(a & MASK)[2:].zfill(16)
        b_bin = bin(b & MASK)[2:].zfill(16)


        carry = 0
        result = []
        for i in range(0, 16):
            A = int(a_bin[15 - i])
            B = int(b_bin[15 - i])

            Q1 = A & B
            Q2 = A ^ B
            Q3 = Q2 & carry
            sum = carry ^ Q2
            carry = Q1 | Q3

            result.insert(0, sum)

        if carry == 1:
            result.insert(0, sum)

        result = int(''.join(map(str, result)), 2)
        if result > MAX_PLUS:
            return -((~result + 1) & MASK)
        return result


if __name__ == "__main__":

    a = -2
    b = -3

    solution = Solution()
    print(solution.getSum(a, b))
