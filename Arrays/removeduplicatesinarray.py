class Solution:
    def removeDuplicates(self, alist):
        unique_elements = {}
        for item in alist:
            if item not in unique_elements:
                unique_elements[item] = True
        
        return list(unique_elements.keys())
    
solution = Solution()
result = solution.removeDuplicates([1,2,3,3,4,5,5,3,22])
print(result)


