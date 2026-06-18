def max_sub_array_of_size_k(nums: list[int], k: int) -> int:
    if len(nums) < k:
        return 0
        
    # Sum of the first window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide the window across the array
    for i in range(len(nums) - k):
        # Subtract the element leaving, add the element entering
        window_sum = window_sum - nums[i] + nums[i + k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum

# Example usage:
nums = [2, 1, 5, 1, 3, 2]
k = 3
result = max_sub_array_of_size_k(nums, k)
print(result)  # Output: 9