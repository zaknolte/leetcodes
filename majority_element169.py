from typing import List
def majorityElement(nums: List[int]) -> int:
    mid = len(nums) // 2
    return sorted(nums)[mid]

print(majorityElement(nums = [2,2,1,1,1,2,2]))