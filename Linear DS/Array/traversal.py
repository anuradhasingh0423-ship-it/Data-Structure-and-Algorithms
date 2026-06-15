marks = [85, 90, 78, 92, 88]

for mark in marks:
    print(mark)

# O(n) where n is the number of elements in the list
# left-right
for i in range(len(marks)):
    print(marks[i])


# reverse
# right- left
for i in range(len(marks)-1, -1, -1):
    print(marks[i])


print("----------")

for mark in reversed(marks):
    print(mark)


print("----------")

for mark in marks[::-1]:
    print(mark)


# nested loop
    
    