from typing import List


class Solution:
    def jump(self, nums: List[int]) -> bool:
        num_jumps = 0
        current_jump = 0
        max_jump = 0

        for i in range(len(nums) - 1):
            max_jump = max(max_jump, i + nums[i])

            if i == current_jump:
                num_jumps += 1
                current_jump = max_jump

        return num_jumps
