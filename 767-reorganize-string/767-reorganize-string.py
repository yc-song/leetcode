'''
Squeezing number into the value with maximum counts returns
the string without any adjacent characters
'''
class Solution:
    def reorganizeString(self, s: str) -> str:
        s = list(s)
        counting_dict = dict() # sorted(list, reverse=True, key=list.count) does not work...
        loop=0

# dictionary whose key is character and value is count -> which can be substituted for counter
        for elem in s:
            try:
                counting_dict[elem] += 1
            except KeyError:
                counting_dict[elem] = 1

# list is reformatted into the list which is sorted by count of characters.
        while counting_dict:
            key = max(counting_dict, key=counting_dict.get)
            for j in range(0, counting_dict[key]):
                s[loop+j]=key
            loop+=counting_dict[key]
            del counting_dict[key]


        max_count = s.count(s[0])

        '''if the maximum value of count is bigger than that of others, 
        there's no mean to get desirable results.'''

        if loop - max_count < max_count - 1:
            return ""
        else:
            for i in range(len(s) - max_count):
                max_idx = [i for i, value in enumerate(s) if value == s[0]]
                # list of indices of maximum count value
                if s[max_count + i] != s[max_idx[0]]:
                    s.insert(max_idx[i % max_count] + 1, s.pop(max_count + i))
                    # squeezing happens

        return ''.join(s)
