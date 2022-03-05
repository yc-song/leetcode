from bisect import bisect_left
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                target=nums[i]+nums[j]
                if target<=nums[j+1]: pass
                else:                 
                    idx=bisect_left(nums, target)
                    ans+=idx-(j+1)
        return ans

#     def binary_search(self, nums:list, start:int, end:int, target:int)->int:
#         if start<end:
#             mid=(start+end)//2
#             # print(start,mid,end, target)
#             if target>nums[mid]:
#                 start=mid+1
#                 return self.binary_search(nums, start, end, target)
#             elif target==nums[mid]: return mid
#             else:
#                 end=mid-1
#                 return self.binary_search(nums, start, end, target)
#         elif target<=nums[start]:
#             # print("1",start)

#             return start

#             # print("2")
#         else: return start+1