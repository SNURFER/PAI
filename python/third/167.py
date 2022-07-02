from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        ret_val = []
        while left < right:
            if numbers[left] + numbers[right] == target:
                ret_val.extend([left + 1, right + 1])
                break

            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

        return ret_val


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSum(numbers, target))

