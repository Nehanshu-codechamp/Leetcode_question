class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # sort first
        n = len(nums)
        result = []

        for i in range(n):
            # Skip duplicate numbers for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            target = -nums[i]  # because nums[i] + nums[left] + nums[right] = 0

            while left < right:
                sum = nums[left] + nums[right]

                if sum == target:
                    # store 3 variables as a triplet
                    triplet = [nums[i], nums[left], nums[right]]
                    result.append(triplet)

                    # Move pointers
                    left += 1
                    right -= 1

                    # Skip duplicates on both sides
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif sum < target:
                    left += 1
                else:
                    right -= 1

        return result
               