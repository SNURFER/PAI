from typing import List


# don't know why this does not work(immutable string)
class Solution(object):
    def reverseString(self, s: List[str]) -> None:
        l_idx: int = 0
        r_idx: int = len(s) - 1

        for i in range(int(len(s) / 2)):
            s[l_idx], s[r_idx] = s[r_idx], s[l_idx]
            l_idx += 1
            r_idx -= 1


if __name__ == "__main__":

    test_str = "ttteststring"

    in_str: List[str] = list(test_str)
    solution = Solution()
    solution.reverseString(in_str)
    print(in_str)
