class Solution:

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distance_dict = dict()
        ans = list()
        distance_list = list()
        i = 0
        for point in points:
            distance = (point[0]) ** 2 + (point[1]) ** 2
            distance_list.append(distance)
            try:
                distance_dict[distance].append(point)
            except:
                distance_dict[distance] = [point]
            i += 1
        kth_num = self.main_finder(distance_list, k)
        for num in kth_num:
            for j in range(len(distance_dict[num])):
                ans.append(distance_dict[num][j])
        return ans

    def main_finder( self,nums: list, idx: int):
        idx -= 1
        return self.finder(nums, 0, len(nums) - 1, idx)

    def finder(self, nums: list, start: int, end: int, idx: int):
        if start == end:
            return set(nums[:start+1])
        else:
            q = self.partition(nums, start, end)
            k = q - start + 1
            if idx < q:
                return self.finder(nums, start, q - 1, idx)
            elif idx > q:
                return self.finder(nums, q + 1, end, idx)
            else:
                return set(nums[:q+1])

    def partition(self, nums: list, start: int, end: int) -> int:
        idx = start - 1
        for i in range(start, end):
            if nums[i] <= nums[end]:
                idx += 1
                nums[i], nums[idx] = nums[idx], nums[i]
        nums[idx + 1], nums[end] = nums[end], nums[idx + 1]
        return idx + 1
