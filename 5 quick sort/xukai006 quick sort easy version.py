#Quick sort

#easy version

'''
Description
@input
    l:      array
    val:    the value to be split
@output
    arr1:   all values in l <= values
    arr2:   all values in l > values
@example:
    #partition([1, 5, 0, 3], 1)
    #-->([0], [5, 3])


'''

def partition(l, val):
    left = []
    right = []
    for element in l:
        if element <= val:
            left.append(element)
        else:
            right.append(element) 
    return left, right


def quickSort(l):
    if len(l) <= 1:
        return l
    elif len(l) == 2:
        if l[0] > l[1]:
            l[0], l[1] = l[1], l[0]
        return l
    else:
        val = l[0]
        left, right = partition(l, val)
        print(l)
        return quickSort(left) + quickSort(right)

res = quickSort([3, 4, 2, 5])
print(res)
print(quickSort([1, 4, 2, 5]))



#def fun():
#    return 1, 2, 3

#a, b, c = fun()
#a=1, b=2, c=3
