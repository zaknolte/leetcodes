class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i.lower() for i in s if i.isalnum()])
        mid = len(s) // 2
        for i in range(mid):
            if s[i] != s[~i]:
                return False
        return True
