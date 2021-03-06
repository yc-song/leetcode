"""
Squeezing number betweens the characters with maximum counts returns
the string without any adjacent characters
"""


class Solution:
    def reorganizeString(self, s: str) -> str:
        s = list(s)
        counting_dict = dict()
        loop = 0

        # 1 dictionary whose key and value is character and count each.
        for elem in s:
            try:
                counting_dict[elem] += 1
            except KeyError:
                counting_dict[elem] = 1

        # 2 list is reformatted into the list which is sorted by counts of characters.
        while counting_dict:
            key = max(counting_dict, key=counting_dict.get)
            for j in range(0, counting_dict[key]):
                s[loop + j] = key
            loop += counting_dict[key]
            del counting_dict[key]

        max_count = s.count(s[0])

        """#3 if the maximum value of count is greater than that of others, 
        there's no means to get desirable results."""

        if loop - max_count < max_count - 1:
            return ""
        else:
            for i in range(len(s) - max_count):
                if not i % max_count:
                    max_idx = [i for i, value in enumerate(s) if value == s[0]]
                if s[max_count + i] != s[max_idx[0]]:
                    s.insert(
                        max_idx[i % max_count] + i % max_count + 1, s.pop(max_count + i)
                    )

        return "".join(s)
