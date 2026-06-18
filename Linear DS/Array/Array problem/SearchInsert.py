class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            # Find the exact middle index
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid  # Target found!
            elif nums[mid] < target:
                low = mid + 1  # Search the right half
            else:
                high = mid - 1  # Search the left half
                
        # If not found, 'low' holds the correct insert position
        return low