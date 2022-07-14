from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        ret_val: List[List[int]] = []

        for man in people:
            ret_val.insert(man[1], man)
        return ret_val


if __name__ == "__main__":
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

    solution = Solution()
    print(solution.reconstructQueue(people))

