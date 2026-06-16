# Same Direction Two Pointers problems
# Amazon question: https://leetcode.com/problems/remove-duplicates-from-sorted-array/


def clean(names):
    left = 0
    for right in range(1, len(names)):
        if names[right] != names[left]:
            left = left + 1
            names[left] = names[right]

    return left + 1
names = ["Alice", "Alice", "Bob", "Bob", "Charlie", "Charlie", "Charlie ", "David", "David", "Eve"  ]
count = clean(names)
print(names[:count])        


"""
same name ? right moves, left stays. Register change does not

different name ? left forward, new name copy left new spot

"""



# for nums

def RemoveDuplicates(nums):
    left = 0
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left = left + 1
            nums[left] = nums[right]
    return left + 1
nums = [1,1,2,3,3,4,5,5,6]
count = RemoveDuplicates(nums)
print(nums[:count])        