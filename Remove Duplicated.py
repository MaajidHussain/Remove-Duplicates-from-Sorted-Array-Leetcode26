class Solution:
    def removeDuplicates(self,nums):
        unique_elements=1
        for index in range(1,len(nums)):
            if nums[index] != nums[index-1]:
                nums[unique_elements] =  nums[index]
                unique_elements+=1
        return unique_elements
        
nums = [0,0,1,1,1,2,2,3,3,4]
solution=Solution()
result=solution.removeDuplicates(nums)
print(result)
print(nums)