class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0    

        nums.sort()
        count = 1
        max_count = 1

        for i in range(0, len(nums) - 1):
            # skip duplicates
            if nums[i + 1] == nums[i]:
                continue

            # consecutive numbers
            if nums[i + 1] == nums[i] + 1:
                count += 1
            else:
                count = 1   # reset if sequence breaks

            max_count = max(max_count, count)
        
        return max_count
