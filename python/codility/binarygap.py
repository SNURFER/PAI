# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    is_count_mode = False
    max_count = 0
    counter = 0
    while N > 0:
        mod_val = N % 2
        if mod_val == 0:
            counter += 1
        else:
            if not is_count_mode:
                is_count_mode = True
            else:
                max_count = max(max_count, counter)

            counter = 0

        N = N // 2

    return max_count


if __name__ == "__main__":
    print(solution(1041))
