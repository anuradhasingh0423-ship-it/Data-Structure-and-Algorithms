marks = [85, 90, 78, 92, 88]

# add to End O(1) --> fast
marks.append(95)
print(marks)

# add to beginning O(n) --> slow
marks.insert(0, 80)
print(marks)

# add to middle O(n) --> slow
marks.insert(3, 89)
print(marks)    

# O(1)
#marks.pop()
marks.pop(1)
print(marks)


# slicing
# O(k) where k is the number of elements in the slice
sub_marks = marks[1:4]
print(sub_marks)