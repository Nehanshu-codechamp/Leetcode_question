class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # handle k > n

        # Helper function to reverse part of the array
        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Step 1: Reverse the entire array
        reverse(nums, 0, n-1)
        # Step 2: Reverse first k elements
        reverse(nums, 0, k-1)
        # Step 3: Reverse remaining elements
        reverse(nums, k, n-1)
