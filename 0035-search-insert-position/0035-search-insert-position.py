class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Brute force solution for the cod
        # for i in range (0,len(nums)):
        #     if nums[i]>=target:
        #         return i
        # return len(nums)        

        # finding lower bound
        start , end = 0,len(nums)-1

        while start<=end:
            mid = (start +end )//2
            if nums[mid]== target:
                 return mid
            elif  nums[mid]<target:
                start  = mid + 1
            else:
                end = mid -1   
        return start         
        