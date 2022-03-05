from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sub_plus: int = 1
        calculated = []

        digits_str = [str(num) for num in digits]
        concat_str = ''.join(digits_str)

        plus_one_val = int(concat_str) + 1

        for ch in str(plus_one_val):
            calculated.append(int(ch))

        return calculated






if __name__ == "__main__":
    solution = Solution()
    input = [1, 2, 5, 6, 9]

    def func(arr):
        arr = 5
    a = 4
    func(a)
    print(a)

    print(solution.plusOne(input))
