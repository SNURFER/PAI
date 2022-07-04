import collections
import heapq
from typing import List


def solution(tickets):
    answer = []
    ticket_dic = collections.defaultdict(list)

    for ticket in sorted(tickets):
        ticket_dic[ticket[0]].append(ticket[1])

    def dfs(start: str, path: List[str]):
        # Tried first in lexicographical order.
        # So, if the value already exists, no further progress is required.
        if len(answer) > 1:
            return

        if len(path) == len(tickets) + 1:
            answer.extend(path)

        # if ticket exists,
        if len(ticket_dic[start]) > 0:
            for i in range(len(ticket_dic[start])):
                dest = ticket_dic[start].pop(i)
                dfs(dest, path + [dest])
                ticket_dic[start].insert(i, dest)

    dfs('ICN', ['ICN'])

    return answer


if __name__ == "__main__":
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    print(solution(tickets))
