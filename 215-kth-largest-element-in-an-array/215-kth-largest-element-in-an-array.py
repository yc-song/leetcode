class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k-=1
        return self.__finder(nums, 0,len(nums)-1, k)
    def __finder(self,nums:list, start:int, end:int, k:int)->int:
        if start==end:
            return nums[start]
        while start<end:
            q = self.__partition(nums, start, end)
            if k>q: # k-th element is bigger than partition index
                return self.__finder(nums, q+1,end, k)

            elif q>k:
                return self.__finder(nums, start, q-1, k)
            else:
                return nums[q]

    def __partition(self,l: list, start: int, end: int) -> int:
        j = start
        for i in range(start + 1, end + 1):
            if l[i] > l[start]:
                j += 1
                l[j], l[i] = l[i], l[j]
        l[start], l[j] = l[j], l[start]
        return j
