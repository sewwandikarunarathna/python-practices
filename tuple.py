#can't change values inside the tuple. so tuples is different from lists.

coordinates = (3, 5, 8)
print(coordinates)
print(coordinates[1])

# coordinates[1] = 10
# print(coordinates) # err is coming bcoz can't assign values to the tuple

#can be used tuples inside lists.
a= [(4,1), (7, 19), (7, 12)]

print(a[1][0])