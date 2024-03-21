from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = values[s[0]]
        for i, letter in enumerate(s[1:]):
            if values[letter] > values[s[i]]:
                total -=  2 * values[s[i]]
            total += values[letter]
        return total

"IX"
"VIII"

a = Solution()
print(a.romanToInt("IX"))