class Solution:
    def maxLength(self, arr: List[str]) -> int:
        resultDict = [""]
        result = 0 
        for word in arr:
            for i in range(len(resultDict)):
                newResult = resultDict[i] + word
                if len(newResult) != len(set(newResult)):
                    continue
                resultDict.append(newResult)
                result = max(result, len(newResult))
        #The time complexity is O(n ^ 2)
        return result
