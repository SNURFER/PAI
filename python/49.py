import collections
from typing import List


class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list[anagrams.values()]


if __name__ == "__main__":
    solution = Solution()

    inputs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(solution.groupAnagrams(inputs))
