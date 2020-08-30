class Solution:
    valueDict = {}
    def calculateVal(self, i, j) -> int:
        indexKey = str(i) + str(j)
        if indexKey in self.valueDict:
            return self.valueDict[indexKey]
        if (j == 1) or (i == j):
            return 1
        value = self.calculateVal(i-1, j-1) + self.calculateVal(i-1, j)
        self.valueDict[indexKey] = value
        return value
    
    def getRow(self, rowIndex: int) -> List[int]:
        valueList = []
        for column in range(rowIndex+1):
            valueList.append(self.calculateVal(rowIndex+1, column+1))
        return valueList
        