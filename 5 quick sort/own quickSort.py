
'''
Description:
    @varibles:
        start: index
        end: index
'''
list1 = [3, 18, 1, 40, 99, 5, 2, 40]


def partition(alist, start, end):
    pivot = alist[start]
    i, j = 0, 0
    for _ in range(0, len(alist)):
        if alist[j] < pivot:
            alist[j], alist[i] = alist[i], alist[j]
            i = i + 1
        j += 1
    j -= 1
    
    print(alist, pivot, 'i', alist[i], 'j', alist[j])
    return i



def quickSort(alist, start, end):
    if start < end:
        i = partition(alist, start, end)
        print(i)
        quickSort(alist, start, i-1)
        quickSort(alist, i+1, end)
        print(alist)


quickSort(list1, 0, 7)
