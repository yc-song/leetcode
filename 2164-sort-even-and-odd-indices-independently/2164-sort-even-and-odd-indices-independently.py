"""
Selection Sort
"""


class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        for i in range(0, len(nums)):
            if not i % 2:  # even
                j = self.find_minimum(
                    nums, i + 1, len(nums)
                )  # find minimum in unsorted list with odd indices.
                nums[i], nums[j] = nums[j], nums[i]
            elif i % 2:  # odd
                j = self.find_maximum(
                    nums, i + 1, len(nums)
                )  # find maximum in unsorted list with even indices.
                nums[i], nums[j] = nums[j], nums[i]
        return nums

    def find_minimum(self, l: list, start: int, end: int) -> int:
        min = start - 1
        for i in range(start, end):
            if l[min] > l[i] and not i % 2:  # find minimum only in even indices.
                min = i
        return min

    def find_maximum(
        self, l: list, start: int, end: int
    ) -> int:  # find maximum in odd indices.
        max = start - 1
        for i in range(start, end):
            if l[max] < l[i] and i % 2:
                max = i
        return max
