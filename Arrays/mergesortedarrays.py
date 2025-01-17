class Solution:
    def mergeSortedArrays(self, alist, blist):
        i, j = 0, 0
        clist = []
        #using two pointers to merge the arrays
        while i<len(alist) and j<len(blist):
            if alist[i] < blist[j]:
                clist.append(i)
                i+=1
            clist.append(j)
            j+=1
        #appending remaining elements of alist
        while i<len(alist):
            clist.append(i)
            i+=1
        #appending remaining elements of blist
        while j<len(alist):
            clist.append(i)
            j+=1
        
        return clist
            
    
solution = Solution()
result = solution.mergeSortedArrays([1,3,4,53],[1, 5, 45])
print(result)