class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ctr = 0  # Initialize counter for valid subarrays
        p = 1    # Initialize product
        start = 0  # Initialize start index for subarray

        for end in range(len(nums)):
            p *= nums[end]  # Update product by multiplying with next element

            # If product is greater than or equal to k, adjust start index and product
            while p >= k and start <= end:
                p /= nums[start]
                start += 1

            # Count subarrays whose product is less than k
            ctr += end - start + 1

        return ctr
        