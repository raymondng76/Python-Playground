from array import array

# array type code 'B' means unsigned char (int)
arr = array('B', range(10))

m1 = memoryview(arr)
print(m1.tolist())
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# cast to another view of shape 2, 5
m2 = m1.cast('B', [2, 5])
print(m2.tolist())
# [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]

# cast to another view of shape 5, 2
m3 = m1.cast('B', [5, 2])
print(m3.tolist())
# [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]

m2[1, 1] = 666
m3[1, 1] = 333

print(arr)
# [0, 1, 2, 333, 4, 5, 666, 7, 8, 9]
