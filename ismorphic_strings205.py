class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        for i in range(len(s)):
            if s[i] not in mapping and t[i] not in mapping.values():
                mapping[s[i]] = t[i]
            elif s[i] not in mapping and t[i] in mapping.values():
                return False
            else:
                if mapping[s[i]] != t[i]:
                    return False
        return True
