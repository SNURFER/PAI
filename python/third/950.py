import collections
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(key=lambda x: -x)
        ret_val = collections.deque([])

        for n in deck:
            if ret_val:
                ret_val.appendleft(ret_val.pop())
            ret_val.appendleft(n)

        return ret_val


if __name__ == "__main__":
    deck = [17, 13, 11, 2, 3, 5, 7]
    solution = Solution()
    print(solution.deckRevealedIncreasing(deck))
