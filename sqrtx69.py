class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        if low > x:
            return x
        while low <= high:
            mid = low + (high - low) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                high = mid - 1
            else:
                low = mid + 1

        return high
