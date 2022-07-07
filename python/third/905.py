import collections
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ret_val = []
        sort_num = collections.deque(nums)

        num_len = len(nums)
        idx_cnt = 0

        while sort_num:
            idx_cnt += 1
            if idx_cnt < num_len:
                num = sort_num.popleft()
                if num % 2 == 1:
                    sort_num.append(num)
                else:
                    ret_val.append(num)
            else:
                ret_val.append(sort_num.popleft())

        return ret_val


if __name__ == "__main__":
    # nums = [3, 1, 2, 4]
    nums = [0, 1, 2]
    solution = Solution()
    print(solution.sortArrayByParity(nums))
