from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(num1: int, num2: int) -> bool:
            return int(str(num1) + str(num2)) < int(str(num2) + str(num1))

        for i in range(len(nums) - 1):
            for j in range(i, len(nums)):
                if compare(nums[i], nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]

        return str(int(''.join(map(str, nums))))


if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9]
    solution = Solution()
    print(solution.largestNumber(nums))
