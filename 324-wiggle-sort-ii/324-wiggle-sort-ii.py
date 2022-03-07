class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort(reverse=True)
        nums[1::2], nums[::2]=nums[0:len(nums)//2], nums[len(nums)//2:]
