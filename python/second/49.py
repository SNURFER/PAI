import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        ana_dict = collections.defaultdict(list)
        for str in strs:
            ana_dict[''.join(sorted(list(str)))].append(str)

        for key in ana_dict:
            output += [ana_dict[key]]

        return output


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    print(solution.groupAnagrams(strs))
