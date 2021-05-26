
f = 1
def search(list,n):
    l = 0
    u = len(list)
    while l<u:
        mid = (l + u) //2
        if n==list[mid]:
            global f
            f=mid
            return True, f
        else:
            if n<list[mid]:
                u = mid - 1

            elif n>list[mid]:
                l = mid + 1
    return False

list = [1,34,576,324,42,24,312,3123,6,3,12,321,5,436,7,78,869,54]
list.sort()
if search(list,7):
    print("Found ")
else:
    print("Not found the value")