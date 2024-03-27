from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        prefix = ""
        while True:
            try:
                if all([word[index] == strs[0][index] for word in strs]):
                    prefix += strs[0][index]
                else:
                    break
                index += 1
            except IndexError:
                break
        return prefix
