class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_num = int(a, 2)
        b_num = int(b, 2)

        sum_ab = a_num + b_num
        return bin(sum_ab)[2:]


if __name__ == "__main__":
    a = "1010"
    b = "1011"
    solution = Solution()
    print(solution.addBinary(a, b))
