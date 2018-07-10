#Youtube videos WebTurning

#selection sort

def selectionSort(sample):
    print('initial list:', sample)

    for i in range(len(sample)):
        print(sample)
        minIndex = i
        j = i + 1
        while(j < len(sample)):
            if(sample[j] < sample[minIndex]):
                minIndex = j
            j += 1
        sample[i], sample[minIndex] = sample[minIndex], sample[i]
    print('sorted list:', sample)

sample1 = [3, 4, 2, 5, 1]
selectionSort(sample1)
