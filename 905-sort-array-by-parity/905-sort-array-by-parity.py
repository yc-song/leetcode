# from collections import deque

class Solution(object):
    
    def sortArrayByParity(self, nums):
        beginning_index, end_index = (
            0,
            len(nums) - 1,
        )
        while beginning_index < end_index:
            if nums[beginning_index] % 2:
                if not nums[end_index] % 2:
                    nums[beginning_index], nums[end_index] = (
                        nums[end_index],
                        nums[beginning_index],
                    )
                    beginning_index += 1  
                end_index -= 1  
            else:
                beginning_index += 1  
        return nums

        