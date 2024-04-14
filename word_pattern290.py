class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        matches = {}
        for i in range(len(pattern)):
            if pattern[i] not in matches and words[i] in matches.values():
                return False
            if pattern[i] not in matches and words[i] not in matches.values():
                matches[pattern[i]] = words[i]
            elif pattern[i] in matches and matches[pattern[i]] != words[i]:
                return False
        return True
