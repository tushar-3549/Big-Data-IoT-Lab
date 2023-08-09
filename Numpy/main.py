# print("Big Data and IoT Lab - Numpy")
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(arr[0])
print(arr[1:3])
print(arr[4:])
print(arr[:4])

arr1 = np.array(['apple', 'banana', 'orange'])
print(arr1.dtype)

a = arr1.copy();
print(a)

arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr2.shape)

arr3 = np.array([1, 2, 3, 4], ndmin=4)
print('Shape of array :', arr3.shape)

arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr4.reshape(4, 3)
print(newarr)

arr5 = np.array([1, 2, 3])
for x in arr5:
  print(x)

arr6 = np.array([1, 2, 3])
arr7 = np.array([4, 5, 6])
arr_con = np.concatenate((arr6, arr7))
print(arr_con)

# array split
ar = np.array([1, 2, 3, 4, 9, 6])
newar = np.array_split(ar, 4)
print(newar)

# search
x = np.where(ar == 4)
print(x)

# sort
print(np.sort(ar))

# filter
filter_arr = []
for element in ar:
  if element > 4:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

nwar = ar[filter_arr]

print(filter_arr)
print(nwar)
