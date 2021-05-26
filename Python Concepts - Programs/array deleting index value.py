# deleting a value at index 2 without using inbuilt function

from array import *
arr = array('i', [11,73,65,45,64])

newarr = array('i',[])

p = int(input('Which index value you want to remove = '))

#program 1 for deleting 1 value
for i in arr:
    if i!=arr[p]:
        newarr.append(i)

#program 2 for deleting value

 #   if p>len(arr):
   #     break
   # if i==arr[p]:
   #     pass
  #  else:
      #  newarr.append(i)


print(newarr)