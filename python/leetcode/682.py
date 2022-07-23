from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        otf_sum = 0
        score = []
        for record in ops:
            if record == '+':
                prev_two_sum = sum(score[-2:])
                otf_sum += prev_two_sum
                score.append(prev_two_sum)
            elif record == 'C':
                invalidate_val = score.pop()
                otf_sum -= invalidate_val
            elif record == 'D':
                double_val = score[-1] * 2
                otf_sum += double_val
                score.append(double_val)
            else:
                otf_sum += int(record)
                score.append(int(record))
        return otf_sum


if __name__ == "__main__":
    ops = ["5", "2", "C", "D", "+"]
    solution = Solution()
    print(solution.calPoints(ops))
