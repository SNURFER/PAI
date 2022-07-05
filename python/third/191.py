class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = bin(n)[2:].count('1')
        return ones

if __name__ == "__main__":
    n = 100
    solution = Solution()
    print(solution.hammingWeight(n))
