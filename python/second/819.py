import collections
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        modified_str = []
        for str in re.sub(r'[^a-zA-Z]', ' ', paragraph).split():
            str = str.lower()
            modified_str.append(str)

        word_cnter = collections.Counter(modified_str)

        for word in word_cnter.most_common():
            if word[0] in banned:
                continue
            return word[0]


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    solution = Solution()
    print(solution.mostCommonWord(paragraph, banned))