from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSum(numbers, target))
