class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # n =len(nums)
        # for i in range(0,n):
           
        #    for j in range(i+1,n):
        #      if nums[i] + nums[j] == target:
        #          return i,j        
        
        n = len(nums)
        hash_map = dict()
        for i in range(n):
            remaining = target - nums[i]
            if remaining in hash_map:
                return [hash_map[remaining], i]
            hash_map[nums[i]] = i