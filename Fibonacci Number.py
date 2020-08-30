class Solution:
    def fib(self, N: int) -> int:
        fibDict = {}
        def calculateFib(n):
            if n in fibDict:
                return fibDict[n]
            if n <= 1: 
                return n
            
            number = calculateFib(n-1) + calculateFib(n-2)
            
            fibDict[n] = number
            
            return number
        
        return calculateFib(N)