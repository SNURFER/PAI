import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        task_dic = collections.Counter(tasks)
        max_count = task_dic.most_common(1)[0][1]
        task_dic[task_dic.most_common(1)[0][0]] = 0
        task_dic += collections.Counter()

        ret_val = (max_count - 1) * (n + 1) + 1
        idle_remain = (max_count - 1) * n

        for task in task_dic:
            task_remain = 1 if task_dic[task] - (max_count - 1) > 0 else 0
            ret_val += task_remain
            if idle_remain > min(task_dic[task], max_count - 1):
                idle_remain -= min(task_dic[task], max_count - 1)
            elif idle_remain == 0:
                ret_val += min(task_dic[task], max_count - 1)
            else:
                ret_val += min(task_dic[task], max_count - 1) - idle_remain
                idle_remain = 0

        return ret_val


if __name__ == "__main__":
    # tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    # n = 2
    ## A _ _ A _ _ A _ _ A _ _ A _ _ A

    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    # tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"]
    # n = 2
    # A _ _ A _ _ A
    solution = Solution()
    print(solution.leastInterval(tasks, n))
