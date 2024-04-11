from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count, ransom_count = defaultdict(int), defaultdict(int)
        for i in magazine:
            magazine_count[i] += 1
        for i in ransomNote:
            ransom_count[i] += 1

        if all([magazine_count[i] >= ransom_count[i] for i in ransom_count]):
            return True
        return False