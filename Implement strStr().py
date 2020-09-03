class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for char in range(len(haystack)-len(needle)+1):
            letters = haystack[char:char+len(needle)]
            if letters == needle:
                return char
        return -1
            