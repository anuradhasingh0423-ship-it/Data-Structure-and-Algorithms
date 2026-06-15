# This function checks for duplicates in a list of numbers 
# by comparing each element with every other element.
# The time complexity of this function is O(n^2) because it uses two nested loops


def has_duplicate_slow(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                return True
    return False  
numbers = [1, 2, 3, 4, 5, 2]

result = has_duplicate_slow(numbers)
if result:
    print("Duplicates found(slow)")
else:
    print("No duplicates found")