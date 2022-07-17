import collections


# def solution(msg):
#     alpha_dict = {
#         'A': 1,
#         'B': 2,
#         'C': 3,
#         'D': 4,
#         'E': 5,
#         'F': 6,
#         'G': 7,
#         'H': 8,
#         'I': 9,
#         'J': 10,
#         'K': 11,
#         'L': 12,
#         'M': 13,
#         'N': 14,
#         'O': 15,
#         'P': 16,
#         'Q': 17,
#         'R': 18,
#         'S': 19,
#         'T': 20,
#         'U': 21,
#         'V': 22,
#         'W': 23,
#         'X': 24,
#         'Y': 25,
#         'Z': 26,
#     }
#     new_num = 27
#
#     answer = []
#     idx = 0
#     while idx < len(msg):
#
#         w_len: int = 1
#         while len(msg[idx: idx + w_len]) == w_len and alpha_dict.get(msg[idx: idx + w_len]) is not None:
#             w_len += 1
#
#         if len(msg[idx: idx + w_len]) == w_len:
#             alpha_dict[msg[idx: idx + w_len]] = new_num
#             new_num += 1
#
#         w_len -= 1
#         answer.append(alpha_dict.get(msg[idx: idx + w_len]))
#
#         idx += w_len
#
#
#     return answer
#
#
# if __name__ == "__main__":
#     msg = "KAKAO"
#     print(solution(msg))

def solution(A, B):
    answer = 0
    A.sort(key=lambda x: x)
    B.sort(key=lambda x: -x)

    for idx, num in enumerate(A):
        answer += num * B[idx]

    return answer


if __name__ == "__main__":

    A = [1, 4, 2]
    B = [5, 4, 4]

    print(solution(A, B))