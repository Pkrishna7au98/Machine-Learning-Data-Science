from array import *

arr= array('i',[1,4,2,7,98,22,55,76])
newarr=array('i',[])
p = len(arr)
j=1
while j<=p:
   newarr.append(arr[p-j])
   j+=1
print(newarr)