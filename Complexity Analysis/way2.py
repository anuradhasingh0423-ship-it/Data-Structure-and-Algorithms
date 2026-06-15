def has_duplicate_fast(numbers):
    seen = set()  # variable seen created (empty set)

    for number in numbers:
        if number in seen:
            return True # if number is already in seen, return True
        seen.add(number) # add number to seen
    return False

numbers = [10,20,30,40,50,10]
result = has_duplicate_fast(numbers)

if result:
    print("Duplicates found(fast)")
else:
    print("No duplicates found")


# The time complexity of this function is O(n)
#  because it iterates through the list of numbers once, 
# and each lookup and insertion operation in the set is on average O(1).


# space complexity is O(n) because in the worst case, 
# if all numbers are unique, the set will store all n numbers.

# space used is more than the O(n^2) approach because it uses additional space for the set,
# while the O(n^2) approach only uses a constant amount of space (O(1)) for the loop variables.