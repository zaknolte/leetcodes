from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # easy solution
        # return [i for i in str(int(''.join([str(i) for i in digits])) + 1)]

        for i in range(len(digits)):
            if digits[~i] == 9:
                digits[~i] = 0
            else:
                digits[~i] += 1
                return digits

        extended = [1]
        extended.extend(digits)
        return extended

