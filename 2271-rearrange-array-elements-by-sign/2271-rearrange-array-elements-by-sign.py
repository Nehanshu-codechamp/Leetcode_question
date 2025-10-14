class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # positive = []
        # negative =[]
        # for j in range (0,len(nums)):
        #     if nums[j]>0:
        #         positive.append(nums[j])
        #     else:
        #          negative.append(nums[j])        

        # for i in range (0,len(positive)):
        #     nums[2*i]=positive[i]
        #     nums[2*i+1]=negative[i]
        # return nums    
# brute force solution hai first
           
           n = len(nums)
           result =[0]*n
           posIndex ,negIndex =0,1
           
           for i in range(0,n):
            if nums[i]>=0:
               result[posIndex] = nums[i]
               posIndex+=2
            else:
                 result[negIndex] = nums[i]
                 negIndex+=2

           return result 