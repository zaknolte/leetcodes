from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] >= len(nums) - 1:
            return True

        jump_size = nums[0]
        for i, num in enumerate(nums):
            jump_size -= 1
            if jump_size < 0:
                return False
            elif num > jump_size:
                jump_size = num
        return True
