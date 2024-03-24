from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_len = len(digits)
        num = 0
        for digit in digits:
            num += digit * pow(10, (num_len - 1))
            num_len -= 1

        num += 1

        ret = []
        while num >= 1:
            ret.append(num % 10)
            num = num // 10

        return ret[::-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))
