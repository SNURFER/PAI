class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


if __name__ == "__main__":
    n = 155
    solution = Solution()
    print(bin(n))
    print(solution.hammingWeight(n))
