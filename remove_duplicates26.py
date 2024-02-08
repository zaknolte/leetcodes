from typing import List
def removeDuplicates(nums: List[int]) -> int:
    seen = {}
    index = len(nums) - 1
    for num in nums[::-1]:
        try:
            if seen[num]:
                nums.pop(index)
        except KeyError:
            seen[num] = True
        index -= 1
    return len(seen)

print(removeDuplicates(nums = [1,1,2]))