marks = [85, 90, 78, 92, 88]

for mark in marks:
    print(mark)

for i in range(len(marks)):
    print(marks[i])


for i in range(len(marks)-1, -1, -1):
    print(marks[i])


print("----------")

for mark in reversed(marks):
    print(mark)


print("----------")

for mark in marks[::-1]:
    print(mark)


    
    