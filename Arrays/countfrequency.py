class Solution:
    def countfrequency(self, alist):
        adict = {}
        for item in alist:
            if item in adict:
                adict[item] +=1
            else:
                adict[item] = 1
        
        return adict
            
    
    

solution = Solution()
result = solution.countfrequency([1,3,3,4,5,5,5])
print(result)