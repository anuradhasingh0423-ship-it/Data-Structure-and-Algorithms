"""
---Sliding Window Technique---

The sliding window technique is a powerful algorithmic approach used to solve problems 
that involve finding a contiguous subarray or substring that satisfies certain conditions. 
It is particularly useful for optimizing problems that would otherwise require nested loops, 
resulting in a more efficient solution.
The basic idea behind the sliding window technique is to maintain a "window" that can expand and
contract as needed while iterating through the data structure (like an array or string).

Here's a general outline of how the sliding window technique works:
1. Initialize two pointers (or indices) to represent the start and end of the window.
2. Expand the end pointer to include more elements in the window until a certain condition is met
    (e.g., the sum of the elements in the window exceeds a target value).
3. Once the condition is met, move the start pointer to shrink the window until the condition is no longer satisfied.
4. Keep track of the best solution found during the process (e.g., the longest substring
    that meets the criteria).
5. Repeat the process until the end pointer reaches the end of the data structure.
The sliding window technique can be applied to a wide range of problems, such as:
- Finding the longest substring without repeating characters.
- Finding the maximum sum of a subarray of a given size.
- Finding the smallest subarray with a sum greater than a given value.
- Finding all anagrams of a string within another string.
- And many more.
By using the sliding window technique, you can often reduce the time complexity of your solution from 
O(n^2) to O(n), making it much more efficient for large input sizes.


"""


def max_sum_subarray(nums, k):
    # 1. Calculate the sum of our very first window
    window_sum = sum(nums[:k])
    max_found = window_sum
    
    # 2. Slide the window across the rest of the array
    for i in range(len(nums) - k):
        # Subtract the element leaving on the left (nums[i])
        # Add the element entering on the right (nums[i + k])
        window_sum = window_sum - nums[i] + nums[i + k]
        
        # Track the highest sum we've seen so far
        max_found = max(max_found, window_sum)
        
    return max_found

# Example usage:
nums = [1, 2, 3, 4, 5]
k = 3
print(max_sum_subarray(nums, k))  # Output: 12 (sum of [3, 4, 5])