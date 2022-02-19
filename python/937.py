from typing import List

class Solution(object):
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_list, letter_list = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digit_list.append(log)
            if log.split()[1].isalpha():
                letter_list.append(log)

        letter_list.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letter_list + digit_list


if __name__ == "__main__":
    solution = Solution()

    log_list: List[str] = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

    print(solution.reorderLogFiles(log_list))
