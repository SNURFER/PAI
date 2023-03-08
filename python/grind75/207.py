import collections
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node_links = collections.defaultdict(list)
        for cur, pre in prerequisites:
            node_links[pre].append(cur)

        trace = set()
        visit = set()

        def dfs(target: int) -> bool:
            if target in trace:
                return False
            if target in visit:
                return True

            trace.add(target)
            for parent in node_links[target]:
                if not dfs(parent):
                    return False

            trace.remove(target)
            visit.add(target)
            return True

        for node in list(node_links):
            ret_val = dfs(node)

            if not ret_val:
                return False

        return True





if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[0, 1]]
    solution = Solution()
    print(solution.canFinish(numCourses, prerequisites))
