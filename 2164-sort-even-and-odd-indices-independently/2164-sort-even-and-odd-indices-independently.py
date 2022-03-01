class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        for i in range(0, len(nums)):
            if not i % 2:  # even
                j = self.find_minimum(nums, i + 1, len(nums))
                nums[i], nums[j] = nums[j], nums[i]
            elif i % 2:
                j = self.find_maximum(nums, i + 1, len(nums))
                nums[i], nums[j] = nums[j], nums[i]
        return nums

    def find_minimum(self, l: list, start: int, end: int) -> int:
        min = start - 1
        for i in range(start, end):
            if l[min] > l[i] and not i % 2:
                min = i
        return min

    def find_maximum(self, l: list, start: int, end: int) -> int:
        max = start - 1
        for i in range(start, end):
            if l[max] < l[i] and i % 2:
                max = i
        return max
