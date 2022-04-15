class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort(reverse=True)
        nums[1::2], nums[::2]=nums[0:len(nums)//2], nums[len(nums)//2:]

    def __quicksorthelp(self, l: list, start: int, end: int) -> None:
        if start < end:
            q = self.__partition(l, start, end)
            self.__quicksorthelp(l, start, q - 1)
            self.__quicksorthelp(l, q + 1, end)
            return
        else:
            return


    def __partition(l: list, start: int, end: int,) -> int:
        j = start
        for i in range(start + 1, end + 1):
            if l[i] > l[start]:
                j += 1
                l[j], l[i] = l[i], l[j]
        l[start], l[j] = l[j], l[start]
        return j
