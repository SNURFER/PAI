class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = self.binToDec(a)
        num_b = self.binToDec(b)
        return self.decToBin(num_a + num_b)

    def binToDec(self, a: str):
        digit: int = 0
        ret: int = 0
        for bit in a[::-1]:
            if bit == '1':
                ret += pow(2, digit)
            digit += 1
        return ret

    def decToBin(self, num: int) -> str:
        return bin(num)[2::]


if __name__ == "__main__":
    solution = Solution()
    print(solution.addBinary('10101', '111'))

