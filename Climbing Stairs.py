class Solution:
    stepMemory = {}
    #Brute Force Recursive Solution
    def climbStairsHelper(self, j: int, n: int) -> int:
        if j == n:
            return 1
        if j > n:
            return 0
        if j in self.stepMemory:
            return self.stepMemory[j]
        self.stepMemory[j] = self.climbStairsHelper(j+1,n) + self.climbStairsHelper(j+2,n)
        return self.stepMemory[j]
    
    def climbStairs(self, n: int) -> int:
        self.stepMemory = {}
        return self.climbStairsHelper(0, n)
    
    #Dynamic Programming Solution
    def climbStairsDynamic(self, n: int) -> int:
        if n in self.stepMemory:
            return self.stepMemory[n]
        if n <= 3:
            return n
        stepCount = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.stepMemory[n] = stepCount
        return stepCount
        