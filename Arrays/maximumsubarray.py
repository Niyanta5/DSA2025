class Solution:
    def maxsubarray(self, alist):
        max_current = alist[0]
        max_global = alist[0]
        
        for i in range(1, len(alist)):
            max_current = max(alist[i], max_current + alist[i])
            if max_current > max_global:
                max_global = max_current
        return max_global
    
    
solution = Solution()
result = solution.maxsubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(result)