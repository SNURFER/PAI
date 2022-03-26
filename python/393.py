from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        def check(size: int) -> bool:
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or data[i] >> 6 != 0b10:
                    return False

            return True

        start = 0
        while start < len(data):
            first = data[start]

            if bin(first >> 3)[2:] == '11110' and check(3):
                start += 4
            elif bin(first >> 4)[2:] == '1110' and check(2):
                start += 3
            elif bin(first >> 5)[2:] == '110' and check(1):
                start += 2
            elif bin(first >> 7)[2:] == '0':
                start += 1
            else:
                return False

        return True


if __name__ == "__main__":
    # data = [197, 130, 1]
    data = [237]
    solution = Solution()
    print(solution.validUtf8(data))