class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numOneDict = {}
        crossoverArray = []
        for num in nums1:
            numOneDict[num] = numOneDict.get(num, 0) + 1
        for num in nums2:
            if num in numOneDict and numOneDict[num] > 0:
                crossoverArray.append(num)
                numOneDict[num] -= 1
        return crossoverArray

                
