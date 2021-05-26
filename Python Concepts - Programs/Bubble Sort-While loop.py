
def sort(list):
    j=0
    while j<=len(list)-j:
        i=0
        while i<len(list)-1:
            if list[i]>list[i+1]:
                list[i],list[i + 1] = list[i+1],list[i]
            i+=1
        j+=1

list = [3,6,21,5,9,7,1,45645,732,42]
sort(list)
print(list)
