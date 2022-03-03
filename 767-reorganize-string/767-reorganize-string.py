class Solution:
    def reorganizeString(self, s: str) -> str:
        s = list(s)
        counting_dict = dict()

        for elem in s:
            try:
                counting_dict[elem] += 1
            except KeyError:
                counting_dict[elem] = 1
        loop=0
        while counting_dict:
            key = max(counting_dict, key=counting_dict.get)
            for j in range(0, counting_dict[key]):
                s[loop+j]=key
            loop+=counting_dict[key]
            del counting_dict[key]
        max_count = s.count(s[0])
        if loop-max_count<max_count-1: return ""
        else:
            for i in range(len(s) - max_count):
                max_idx = [i for i, value in enumerate(s) if value == s[0]]

                if s[max_count + i] != s[max_idx[0]]:

                    s.insert(max_idx[i % max_count] + 1, s.pop(max_count + i))
                # print(s)

            return ''.join(s)
