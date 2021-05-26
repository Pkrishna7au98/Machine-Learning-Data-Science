
def sort(list):
    j=0
    for j in range(len(list)-j):
        for i in range(len(list)-1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
            i+=1
list = [3,6,21,7,1,45645,732,6435,3243242,6657,23,676,4332]
sort(list)

print(list)w