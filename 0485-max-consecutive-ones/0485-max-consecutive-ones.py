class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
       count = 0
       max_count =0
       for i in range (0,len(nums)):
        if nums[i] == 1:
            count+=1
        else:
            # ye tab run hoga jab 0 encounter karega, nums me 
            max_count = max(max_count,count)
            count =0   
        ans = max(max_count,count) 
       return ans
        # ye jaruri hai kuki agar last me max no of 1 mil gaye toh else kabhi run nahi hoga  
       
        