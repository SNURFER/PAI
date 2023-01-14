import sys
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret_val = []
        merge_min = sys.maxsize
        merge_max = -sys.maxsize
        start, end = newInterval
        has_merge_scope = False
        need_no_merge = False

        if not intervals:
            ret_val.append([start, end])


        for pair in intervals:
            if not has_merge_scope and end < pair[0] and need_no_merge is False:
                need_no_merge = True
                ret_val.append([start, end])

            if pair[1] < start:
                ret_val.append(pair)

            elif pair[0] > end:
                if has_merge_scope:
                    has_merge_scope = False
                    ret_val.append([merge_min, merge_max])
                ret_val.append(pair)
            else:
                has_merge_scope = True
                need_no_merge = True
                merge_min = min(merge_min, min(start, pair[0]))
                merge_max = max(merge_max, max(end, pair[1]))

        if has_merge_scope:
            ret_val.append([merge_min, merge_max])

        if intervals and intervals[-1][1] < start:
            ret_val.append([start, end])

        return ret_val


if __name__ == "__main__":
    # intervals = [[1, 3], [6, 9]]
    # intervals = [[6, 8]]
    # newInterval = [1, 5]
    # intervals = [[1, 5]]
    # newInterval = [6, 8]
    intervals = [[3, 5], [12, 15]]
    newInterval = [6, 7]
    solution = Solution()
    print(solution.insert(intervals, newInterval))