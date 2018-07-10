#bubble sort two foor loop


list1 = [3, 4, 2, 1, 5]
list2 = [89, 45, 2, 49, 10, 21]


def bubbleSort(alist):
    for i in range(len(alist)-1):
        for j in range(len(alist)-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
            print(alist)
            
#bubbleSort(list1)
#print(list1)
bubbleSort(list2)
print(list2)
