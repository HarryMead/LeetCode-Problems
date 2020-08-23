class Solution:  
	#O(n^2) solution
    #def rotate(self, nums: List[int], k: int) -> None:
    #    for j in range(k):
    #        for i in range(len(nums) - 1,0,-1):
    #            nums[i], nums[i-1] = nums[i-1], nums[i]
    
	#O(n) solution
    def rotate(self, nums: List[int], k: int) -> None:
        tempArray = nums.copy()
        for i in range(len(nums)):
            newIndex = (i + k) % len(nums)
            tempArray[newIndex] = nums[i]
        nums[:] = tempArray
