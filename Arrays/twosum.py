from typing import List
class Solution:
    def twoSum(self, alist:List[int], target:int) -> List[int]:
        result = []
        adict = {}
        for i, num in enumerate(alist):
            complement = target-num
            if complement in adict:
                result.append([adict[complement], i])
            adict[num] = i
        return result
    
solution = Solution()
finalresult = solution.twoSum([1,3,53,3,2,4],6)
print(finalresult)        