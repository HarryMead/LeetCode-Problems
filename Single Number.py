class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        newList = []
        for num in nums[:]:
            if num not in newList:
                newList.append(num)
                nums.remove(num)        
        main_list = list(set(newList).difference(nums))
        return main_list[0]
        