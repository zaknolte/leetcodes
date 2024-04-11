class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        if not s:
            return True
        else:
            try:
                for letter in t:
                    if letter == s[idx]:
                        idx += 1
            finally:
                return idx >= len(s)