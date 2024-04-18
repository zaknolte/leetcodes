class Solution:
    def isHappy(self, n: int) -> bool:
        is_happy = False
        seen_n = []
        def sum_squares(num):
            sums = 0
            while num > 0:
                i = num % 10
                sums += i * i
                num = num // 10
            return sums
        calculating = True
        while calculating:
            n = sum_squares(n)
            if n == 1:
                is_happy = True
                calculating = False
            elif n in seen_n:
                calculating = False
            seen_n.append(n)

        return is_happy

a = Solution()
a.isHappy(19)