import collections
import re
from typing import List


class Solution(object):
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        modified_word: List[str] = [word.lower() for word in re.sub(r'[^\w]', ' ', paragraph).split() if
                                    word not in banned]

        dic_word = collections.defaultdict(int)
        for word in modified_word:
            dic_word[word] += 1

        return max(dic_word, key=dic_word.get)


if __name__ == "__main__":
    solution = Solution()
    para = "Bob hit a ball, the hit BALL flew far after it was hit."
    ban = ["hit"]
    print(solution.mostCommonWord(para, ban))
