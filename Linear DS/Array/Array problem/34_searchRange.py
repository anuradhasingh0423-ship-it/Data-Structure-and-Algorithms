class Solution(object):
    def searchRange(self, nums, target):
        def find_bound(is_first):
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        first_pos = find_bound(is_first=True)
        if first_pos == -1:
            return [-1, -1]
        last_pos = find_bound(is_first=False)
        
        return [first_pos, last_pos]

# ========================================================
# THE TEST DRIVER
# ========================================================
if __name__ == "__main__":
    
    solution = Solution()
    
    # Test Case 1: Target present with duplicates
    nums1, target1 = [5, 7, 7, 8, 8, 10], 8
    result1 = solution.searchRange(nums1, target1)
    
    # Test Case 2: Target missing
    nums2, target2 = [5, 7, 7, 8, 8, 10], 6
    result2 = solution.searchRange(nums2, target2)
    
    # Test Case 3: Empty array
    nums3, target3 = [], 0
    result3 = solution.searchRange(nums3, target3)

    print("-" * 55)
    print(f"🎬 Test 1: nums={nums1}, target={target1} -> Output: {result1}")
    print(f"🎬 Test 2: nums={nums2}, target={target2} -> Output: {result2}")
    print(f"🎬 Test 3: nums={nums3}, target={target3}             -> Output: {result3}")
    print("-" * 55)