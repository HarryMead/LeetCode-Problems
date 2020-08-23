#Manual python solution
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

#This is the obvious python solution			
class SolutionTwo:
    def reverseString(self, s: List[str]) -> None:
        s.reverse();
        
        

        
        
        