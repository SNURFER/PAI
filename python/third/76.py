import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        include_flag: bool = False
        window = []

        min_str = s
        t_cnt = collections.Counter(t)

        for ch in s:
            window.append(ch)
            t_cnt[ch] -= 1

            # exception...
            if ch not in t:
                t_cnt[ch] += 1

            # if all elements are included in window
            if t_cnt.most_common(1)[0][1] <= 0:
                include_flag = True
                while True:
                    left_ch = window[0]
                    if left_ch in t and t_cnt[left_ch] >= 0:
                        break
                    elif left_ch in t:
                        window.pop(0)
                        t_cnt[left_ch] += 1
                    else:
                        window.pop(0)

                win_str = ''.join(window)
                min_str = min_str if len(min_str) <= len(win_str) else win_str

        if not include_flag:
            return ""
        return min_str


if __name__ == "__main__":
    # s = "A"
    # t = "AA"
    # s = "ADOBECODEBANC"
    # t= "ABC"
    s = "baaaabab"
    t= "abb"
    solution = Solution()
    print(solution.minWindow(s, t))

