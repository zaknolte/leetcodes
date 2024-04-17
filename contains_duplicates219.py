from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        for i, num in enumerate(nums):
            if num not in index_map:
                index_map[num] = i
            else:
                if abs(i - index_map[num]) <= k:
                    return True
                else:
                    index_map[num] = i
        return False