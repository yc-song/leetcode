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
            # print(loop,j,s)
            loop+=counting_dict[key]
            del counting_dict[key]
        max_count = s.count(s[0])
        for i in range(len(s) - max_count):
            max_idx = [i for i, value in enumerate(s) if value == s[0]]

            if s[max_count + i] != s[max_idx[0]]:
                # print(max_idx, i%max_count, max_count+i)

                s.insert(max_idx[i % max_count] + 1, s.pop(max_count + i))
            # print(s)
        for j in range(len(s) - 1):
            if s[j] == s[j + 1]: return ""
        return ''.join(s)