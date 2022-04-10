import collections
import heapq
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # ticket_dict = collections.defaultdict(list)
        #
        # output = []
        #
        # for ticket in tickets:
        #     heapq.heappush(ticket_dict[ticket[0]], ticket[1])
        #
        # def dfs(depth: int, dest: str, path: List[str]):
        #     start: str = dest
        #     if depth == len(tickets):
        #         output.append(path)
        #         return
        #     if not len(ticket_dict[start]):
        #         return
        #
        #     dest_candidate: List[str] = ticket_dict[start]
        #
        #     while dest_candidate:
        #         new_dest = dest_candidate.pop(0)
        #         dfs(depth + 1, new_dest, path + [new_dest])
        #
        # dfs(0, 'JFK', ['JFK'])
        # return output[0]
        graph = collections.defaultdict(list)

        for land, dest  in sorted(tickets):
            graph[land].append(dest)

        output = []
        def dfs(land: str):
            while graph[land]:
                arrival: str = graph[land].pop(0)
                dfs(arrival)
            output.append(land)

        dfs('JFK')

        return output[::-1]


if __name__ == "__main__":
    # tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    # tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]

    tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    solution = Solution()
    print(solution.findItinerary(tickets))

