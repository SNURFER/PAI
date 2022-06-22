from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret_val = []

        merged_val = []
        for interval in intervals:
            if not merged_val:
                merged_val = interval
            elif interval[0] <= merged_val[1]:
                if merged_val[1]  < interval[1]:
                    merged_val[1] = interval[1]
            else:
                ret_val.append(merged_val)
                merged_val = interval

        if merged_val:
            ret_val.append(merged_val)

        return ret_val


if __name__ == "__main__":
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = [[1, 4], [2, 3]]
    solution = Solution()
    print(solution.merge(intervals))
