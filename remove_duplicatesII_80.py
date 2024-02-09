from typing import List
def removeDuplicates(nums: List[int]) -> int:
    seen = {}
    index = len(nums) - 1
    for num in nums[::-1]:
        try:
            if seen[num] > 2:
                nums.pop(index)
        except KeyError:
            seen[num] = 1
        index -= 1
        seen[num] += 1
    return len(nums), nums

print(removeDuplicates(nums = [0,0,1,1,1,1,2,3,3]))