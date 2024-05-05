from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target == nums[0]:
            return 1
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (high + low) // 2
            if nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid
            elif nums[mid] == target:
                return mid
            if high - low == 1:
                return high
