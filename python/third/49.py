import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = collections.defaultdict(list)
        out = []

        for word in strs:
            temp = ''.join(sorted(list(word)))
            ana_dict[temp].append(word)

        for key in ana_dict:
            out.append(ana_dict[key])

        return out


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    solution = Solution()
    print(solution.groupAnagrams(strs))
