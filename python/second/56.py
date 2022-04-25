from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge_list = []
        intervals.sort()

        prev = intervals[0]
        for interval in intervals:
            if prev[1] >= interval[0]:
                prev[1] = max(interval[1], prev[1])
            else:
                merge_list.append(prev)
                prev = interval

        if prev not in merge_list:
            merge_list.append(prev)
        return merge_list


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    solution = Solution()
    print(solution.merge(intervals))