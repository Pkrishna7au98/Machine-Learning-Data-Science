from numpy import *

arr1 =([1,40,5])
arr2 =([21,33,45])

newarr = arr1.copy()

p=0
for i in arr1:
    newarr[p] = i + arr2[p]
    p += 1

print(arr1)
print(arr2)

print(newarr)
