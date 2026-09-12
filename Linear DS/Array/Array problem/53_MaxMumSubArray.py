class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        current_sum = 0
        
        for num in nums:
            # If current_sum is negative, reset it to 0 (start fresh)
            if current_sum < 0:
                current_sum = 0
                
            current_sum += num
            max_sum = max(max_sum, current_sum)
            
        return max_sum

# Example usage:
solution = Solution()
result = solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(result)