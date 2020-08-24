class Solution:
    #A slow solution of time complexity O(n^2)
    def firstUniqCharSlow(self, s: str) -> int:
        check = False
        for char in range(len(s)):
            if s.count(s[char]) < 2:
                check = True
                return char
        if not s or check == False:
            return -1
        
    #A faster solution of time complexity O(1)
    def firstUniqChar(self, s: str) -> int:
        hashTable = collections.Counter(s)
        
        for idx, ch in enumerate(s):
            if hashTable[ch] == 1:
                return idx
    
        return -1
        

        