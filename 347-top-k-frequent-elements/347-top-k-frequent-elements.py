
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counting_dict=Counter(nums)
        sorted_dict=sorted(counting_dict.items(), key= lambda item:item[1], reverse= True)
        ans=[None]*k
        for i in range(k):
            ans[i]=sorted_dict[i][0]
        return ans
        