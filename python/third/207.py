import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        # init graph
        for c, p in prerequisites:
            graph[c].append(p)

        trace = set()
        visit = set()

        def dfs(target):
            if target in trace:
                return False
            if target in visit:
                return True

            trace.add(target)
            for required in graph[target]:
                if not dfs(required):
                    return False

            trace.remove(target)
            visit.add(target)
            return True

        ret_val = True
        for course in list(graph):
            ret_val = dfs(course)
            if not ret_val:
                return ret_val

        return ret_val


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    solution = Solution()
    print(solution.canFinish(numCourses, prerequisites))
