class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        result = [1] * n

        # Calculate left products
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        # Calculate right products
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]

        # Calculate final result
        for i in range(n):
            result[i] = left_products[i] * right_products[i]

        return result
        
        
        