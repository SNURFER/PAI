

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = [int(x) for x in str(n)]

        product = 1
        total_sum = 0
        for num in res:
            product *= num
            total_sum += num
        print(product - total_sum)
        return product - total_sum


if __name__ == "__main__":
    solution = Solution()
    solution.subtractProductAndSum()
