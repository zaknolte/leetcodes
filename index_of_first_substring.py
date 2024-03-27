import re
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = re.search(f"({needle})", haystack)
        return idx.start(1) if idx is not None else -1