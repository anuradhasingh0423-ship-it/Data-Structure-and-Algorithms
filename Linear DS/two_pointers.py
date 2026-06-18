"""
----Two Pointers Technique----

The two pointers technique is a common algorithmic approach used to solve problems involving arrays or linked lists.
It involves using two pointers to traverse the data structure in a coordinated manner, often starting from different ends or positions.

Here's a general outline of how the two pointers technique works:
1. Initialize two pointers at specific positions (e.g., one at the beginning and one at the end of an array).
2. Move the pointers based on certain conditions until a desired state is reached.
3. Keep track of the best solution found during the process.
4. Repeat the process until the pointers meet or cross each other.

The two pointers technique can be applied to a wide range of problems, such as:
- Finding a pair of numbers in a sorted array that sum up to a target value.
- Removing duplicates from a sorted array.
- Checking if a string is a palindrome.
- And many more.

By using the two pointers technique, you can often reduce the time complexity of your solution from O(n^2) to O(n),
making it much more efficient for large input sizes.

"""





def find_two_numbers(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return [numbers[left], numbers[right]]
        
        elif total > target:
            right = right - 1
        else:
            left = left - 1
    return []        

numbers = [1,3,5,6,8,11]

print(find_two_numbers(numbers, 9))
print("-------------")
print(find_two_numbers(numbers, 14))
print("-------------")
print(find_two_numbers(numbers, 16))