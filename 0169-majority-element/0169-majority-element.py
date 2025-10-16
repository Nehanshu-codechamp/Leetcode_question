class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map ={}
        for i in range(0,len(nums)):
            if nums[i] in freq_map:
                freq_map[nums[i]]+=1
            else:
                freq_map[nums[i]]=1

        max_count = 0
        majority = None

        for k, v in freq_map.items():
            if v > max_count:
                max_count = v
                majority = k

        return majority        