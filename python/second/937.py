from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        output_str = []
        output_digit = []
        for log in logs:
            if log.split()[1].isdigit():
                output_digit.append(log)
            else:
                output_str.append(log)

        output_str.sort(key=lambda x:(x.split()[1:], x.split()[0]))
        output = []
        output += output_str + output_digit
        return output


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    solution = Solution()
    print(solution.reorderLogFiles(logs))
