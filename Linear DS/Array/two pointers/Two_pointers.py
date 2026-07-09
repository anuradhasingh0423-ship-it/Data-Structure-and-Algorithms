def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need a larger sum, move left pointer right
        else:
            right -= 1 # Need a smaller sum, move right pointer left
            
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum_sorted(nums, target)
print(result)  # Output: [0, 1]