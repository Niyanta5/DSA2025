class Solution:
    def findMinElement(self, alist):
        min_element = alist[0]
        for i in range(1, len(alist)):
            if alist[i]<min_element:
                min_element = alist[i]
            
        return min_element
    
    
solution = Solution()
result = solution.findMinElement([11,35,3,32,5,2])
print(result)