#selection sort



#not in place

#step0: create a new array
#step1: find the min number in the list
#step2: append current min number in the new array
#step3: delete this min number
#step4: ##continue to find the min number

#list1 = [2, 4, 5, 1, 3]
list2 = [89, 45, 2, 49, 10, 21]

def minFunc(alist):
    for i in range(len(alist)):
        if alist[i] < alist[0]:
            alist[0], alist[i] = alist[i], alist[0]
    return alist[0]

def selectionSort1(alist):
    newList = []
    for i in range(len(alist)):
        minNum = minFunc(alist)
        newList.append(minNum)
        alist.remove(minNum)
    return newList

#print(selectionSort1(list1))
#print(selectionSort1(list2))




#in place

#step1: let i be the very first idx, and then i++
#step2: find the min number in the list and change values between alist[i] alist[j]
#step3: swap
list3 = [2, 4, 5, 1, 3]
list4 = [89, 45, 2, 49, 10, 21]


def selectionSort2(alist):
    for i in range((len(alist)-1), -1, -1):
        for j in range(0, i):
            if i != j and alist[i] < alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
            print(alist)
    return alist

#print(selectionSort2(list3))
print(selectionSort2(list4))
