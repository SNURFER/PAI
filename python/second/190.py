class Solution:
    def reverseBits(self, n: int) -> int:
        bin_list = list(bin(n)[2:].zfill(32))

        def divAndCon(left: int, right: int):
            if left == right:
                return
            # mid index
            mid = left + (right - left) // 2

            # divide
            divAndCon(left, mid)
            divAndCon(mid + 1, right)

            # conquer
            for i in range(left, mid + 1):
                bin_list[i], bin_list[mid + 1 + i - left] = bin_list[mid + 1 + i - left], bin_list[i]

        divAndCon(0, 31)
        reversed_bit = int(''.join(bin_list), 2)

        return reversed_bit


if __name__ == "__main__":
    n = 43261596
    # n = 00000010100101000001111010011100
    solution = Solution()
    print(solution.reverseBits(n))
