import collections
import heapq
from typing import List


class Solution:
    result = List[str]
    found = False

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # init ticket dict
        ticket_dict = collections.defaultdict(list)
        for ticket in tickets:
            # ticket[0] is departure, ticket[1] is arrival.
            ticket_dict[ticket[0]].append(ticket[1])

        def bt(depth: int, depart: str, path: List[str]):
            if self.found:
                return

            if depth == len(tickets):
                self.found = True
                self.result = path
                return

            if not ticket_dict[depart]:
                return

            for dest in sorted(ticket_dict[depart]):
                ticket_dict[depart].remove(dest)
                bt(depth + 1, dest, path + [dest])
                ticket_dict[depart].append(dest)

        bt(0, "JFK", ["JFK"])
        return self.result


if __name__ == "__main__":
    # tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    # tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    # tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    tickets = [["EZE","TIA"],["EZE","AXA"],["AUA","EZE"],["EZE","JFK"],["JFK","ANU"],["JFK","ANU"],["AXA","TIA"],["JFK","AUA"],["TIA","JFK"],["ANU","EZE"],["ANU","EZE"],["TIA","AUA"]]
    solution = Solution()
    print(solution.findItinerary(tickets))
