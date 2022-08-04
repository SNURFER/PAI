from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path_list = []
        def dfs(target: int, depth: int, path: List[int]):
            if target == len(graph) - 1:
                path_list.append(path)
                return

            for next_target in graph[target]:
                dfs(next_target, depth + 1, path + [next_target])

        dfs(0, 1, [0])

        return path_list


if __name__ == "__main__":
    graph = [[1, 2], [3], [3], []]
    # graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    solution = Solution()
    print(solution.allPathsSourceTarget(graph))
