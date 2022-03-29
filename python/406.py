import heapq
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))

        result = []
        for per in people:
            result.insert(per[1],[per[0], per[1]])
        # heap = []
        # for person in people:
        #     heapq.heappush(heap, (-person[0], person[1]))
        # result = []
        # while heap:
        #     person = heapq.heappop(heap)
        #     result.insert(person[1], [-person[0], person[1]])
        return result


if __name__ == "__main__":
    # people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
    # people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    # people = [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]
    people = [[7, 0], [3, 0], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]
    solution = Solution()
    print(solution.reconstructQueue(people))