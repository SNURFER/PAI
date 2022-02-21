from typing import List


class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        left_ptr: int
        right_ptr: int

        output: List[List[int]] = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left_ptr = i + 1
            right_ptr = len(nums) - 1
            while left_ptr < right_ptr:
                sum_val: int = nums[i] + nums[left_ptr] + nums[right_ptr]
                if sum_val == 0:
                    if not [nums[i], nums[left_ptr], nums[right_ptr]] in output:
                        output.append([nums[i], nums[left_ptr], nums[right_ptr]])
                    right_ptr -= 1
                    left_ptr += 1
                elif sum_val > 0:
                    right_ptr -= 1
                else:
                    left_ptr += 1

        return output


if __name__ == "__main__":
    solution = Solution()
    # num_list = [-1, 0, 1, 2, -1, -4]
    # num_list = [1, -1, -1, 0]
    num_list = [-2, 0, 0, 2, 2]

    print(solution.threeSum(num_list))
