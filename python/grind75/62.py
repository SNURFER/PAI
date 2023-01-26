class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(num: int) -> int:
            if num <= 1:
                return 1
            return factorial(num - 1) * num

        return int(factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1)))


if __name__ == "__main__":
    m = 3
    n = 7
    solution = Solution()
    print(solution.uniquePaths(m, n))
