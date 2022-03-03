"""
in
"""


class Solution(object):
    def sortArrayByParity(self, nums) -> list:
        left_index, right_index = (
            0,
            len(nums) - 1,
        )
        while left_index < right_index:
            if nums[left_index] % 2:  # odd
                if not nums[right_index] % 2:  # even
                    nums[left_index], nums[right_index] = (
                        nums[right_index],
                        nums[left_index],
                    )
                    # swap happens when odd is at the left end and even is at the right end
                    left_index += 1
                right_index -= 1  # end index moves leaving odd integer intact
            else:
                left_index += 1  #
        return nums
