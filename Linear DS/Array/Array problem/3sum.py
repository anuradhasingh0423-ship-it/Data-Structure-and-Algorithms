class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # Step 1: Sort the array to make pointer navigation and duplicate skipping easy
        nums.sort()
        n = len(nums)
        
        # Step 2: Fix the first element 'i'
        for i in range(n - 2):
            # If the current fixed number is positive, it's impossible to sum to 0
            # because all remaining numbers to its right are also positive!
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the fixed position
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 3: Initialize Two Pointers for the remaining window
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for the 'left' pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for the 'right' pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # Move both pointers inward to look for other pairs with this same 'i'
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    # Our sum is too small, we need a larger number. Move left pointer right.
                    left += 1
                else:
                    # Our sum is too big, we need a smaller number. Move right pointer left.
                    right -= 0
                    right -= 1
                    
        return res