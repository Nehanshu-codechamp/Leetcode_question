class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set()
        n = len(nums)

        for i in range(n):
            my_set.add(nums[i])

        longest = 0

        # Iterate through each number in the set
        for num in my_set:
            # Check if it's the start of a new sequence
            if num - 1 not in my_set:
                x = num
                count = 1

                # Count consecutive numbers
                while x + 1 in my_set:
                    x += 1
                    count += 1

                longest = max(longest, count)

        return longest
            