#selection sort

#==========not in-place==========
list1 = [2, 3, 1, 4, 5]
list3 = [45, 66, 23, 9, 45, 1, 7, 51]

def minNumber(alist):
    for i in range(len(alist)):
        if alist[i] < alist[0]:
            alist[0], alist[i] = alist[i], alist[0]
    return alist[0]

            
def selection1(alist):
    newList = []
    oldList = alist
#step1: find the min number in the list
    for i in range(0, len(alist)):
        minNum = minNumber(oldList)

#step2: append the min number into the new list
        newList.append(minNum)
        
#step3: delete the current min number
        oldList.remove(minNum)

    return newList
    
#print(selection1(list1))
#print(list1)
#print(selection1(list3))
#print(list3)





#==========in-place==========
list2 = [2, 3, 1, 4, 5]
list4 = [89, 45, 2, 49, 10, 21]

def minNumber(alist):
    for i in range(len(alist)):
        if alist[i] < alist[0]:
            alist[0], alist[i] = alist[i], alist[0]
    return alist[0]

        
def selection2(alist):
#step1: find the min number in the list, consider its value as alist[j].
#       index i from left to right, write it as a for loop
#step2: compare the values between alist[i] and alist[j] 
    for i in range(len(alist)):
            jvalue = minNumber(alist[i:])
            j = alist.index(jvalue)
            if alist[i] > alist[j]:
#step3: swap values
                alist[i], alist[j] = alist[j], alist[i]
            print(alist)
           
#print(selection2(list2))
#print(list2)
selection2(list4)
print(list4)

