class Solution:
    def removeElement(self, alist, num):
        blist = []
        for i in range(0, len(alist)):
            if alist[i] != num:
                blist.append(alist[i])
                
        #return the length of the remaining elements after deleting all the occurrences of val
        return len(blist)
    
    
solution= Solution()
result = solution.removeElement([1,34,2, 4, 4,4,4], 4)
print(result)