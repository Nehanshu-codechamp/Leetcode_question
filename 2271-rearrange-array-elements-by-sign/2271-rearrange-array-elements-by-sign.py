class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative =[]
        for j in range (0,len(nums)):
            if nums[j]>0:
                positive.append(nums[j])
            else:
                 negative.append(nums[j])        

        for i in range (0,len(positive)):
            nums[2*i]=positive[i]
            nums[2*i+1]=negative[i]
        return nums    
