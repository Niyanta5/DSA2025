class Solution:
    #sorting the array using insertion sort
    def insertionsort(self, nums):
        for i in range(1, len(nums)):
            key = nums[i] #key is the current pos
            j = i-1
            while j>=0 and nums[j]>key:
                nums[j+1] = nums[j]
                j-=1
            nums[j+1]  = key
        return nums      
    

    #now searching the insert position
    def search_insert_pos(self, nums, target):
        sorted_nums = self.insertionsort(nums)
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left +=1
            else:
                right -=1
        
        return left
        
        
    
    
solution = Solution()
result = solution.search_insert_pos([1,3,45,3333,32], 32)
print(result)