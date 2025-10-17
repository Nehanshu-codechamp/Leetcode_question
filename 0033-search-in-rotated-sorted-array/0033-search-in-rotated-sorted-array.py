class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # n = len(nums)
        # for i in range(0,n):
        #     if nums[i]== target:
        #         return i
        # return -1        
        n = len(nums)
        start,end = 0,n-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid]== target:
                return mid

            if nums[mid]<nums[end]:
                if nums[mid]<=target<=nums[end]:
                    start =mid+1
                else:
                    end = mid -1    

            else:
                if nums[start]<=target<=nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
        return -1
                    