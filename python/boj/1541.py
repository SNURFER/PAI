import sys

input = sys.stdin.readline

def solution():
    formula = input()

    min_cal = 0
    accum_ch = ''
    met_first_minus = False
    for ch in formula:
        if ch.isdigit():
            accum_ch += ch
        else:
            if met_first_minus:
                min_cal -= int(accum_ch)
            else:
                if ch == '-':
                    met_first_minus = True
                min_cal += int(accum_ch)
            accum_ch = ''

    print(min_cal)


if __name__ == "__main__":
    solution()
