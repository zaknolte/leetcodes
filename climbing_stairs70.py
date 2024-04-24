class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        a = 2
        b = 3
        for i in range(4, n + 1):
            steps = a + b
            a = b
            b = steps

        return steps
