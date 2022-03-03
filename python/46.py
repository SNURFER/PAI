from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(index: int, permute_list: List[int]):
            if len(permute_list) == len(nums):
                ret_val.append(permute_list[:])
                return
            for j in range(len(nums)):
                if not visited[j]:
                    visited[j] = True
                    permute_list.append(nums[j])
                    dfs(index + 1, permute_list)
                    permute_list.remove(nums[j])
                    visited[j] = False

        ret_val = []
        visited = [False] * len(nums)
        for i in range(len(nums)):
            visited[i] = True
            dfs(0, [nums[i]])
            visited[i] = False

        return ret_val


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 3, 4]

    print(solution.permute(nums))
