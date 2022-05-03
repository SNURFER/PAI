class Solution:
    def hammingWeight(self, n: int) -> int:
        res = [int(x) for x in str(bin(n)[2:])]
        return res.count(1)


if __name__ == "__main__":
    n = 19
    solution = Solution()
    print(solution.hammingWeight(n))
