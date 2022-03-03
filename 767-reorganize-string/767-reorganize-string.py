from collections import deque
class Solution:
    def reorganizeString(self, s: str) -> str:
        s = list(s)
        s_sorted = deque()
        counting_dict = dict()

        for elem in s:
            try:
                counting_dict[elem] += 1
            except KeyError:
                counting_dict[elem] = 0

        while counting_dict:
            key = max(counting_dict, key=counting_dict.get)
            for j in range(counting_dict[key] + 1):
                s_sorted.append(key)
            del counting_dict[key]

        max_count = s_sorted.count(s_sorted[0])
        for i in range(len(s) - max_count):
            max_idx = [i for i, value in enumerate(s_sorted) if value == s_sorted[0]]

            if s_sorted[max_count + i] != s_sorted[max_idx[0]]:
                s_sorted.insert(max_idx[i % max_count] + 1, s_sorted[max_count + i])
                del s_sorted[max_count+i+1]
        for j in range(len(s_sorted) - 1):
            if s_sorted[j] == s_sorted[j + 1]: return ""
        return ''.join(s_sorted)
