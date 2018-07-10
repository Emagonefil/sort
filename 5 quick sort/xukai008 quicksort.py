"""
partition(A, lo, hi)

Partition an array A from lo to hi.
"""
def partition(A, lo, hi):   # lo: low, hi: high
    val = A[lo]   # pivot
    i, j = lo, hi + 1
    while i < j:
        # do {
        #   ...
        # } while (condition)
        while True and i < hi:
            i += 1
            if A[i] > val:
                break
        # After this loop, A[i] > val
        while True and j > lo:
            j -= 1
            if A[j] <= val:
                break
        # After this loop, A[j] < val
        # Swap A[i], A[j]
        # print("Before", A, "i", i, "j", j)
        if i >= j:
            break
        A[i], A[j] = A[j], A[i]
        # print("After", A)
    A[j], A[lo] = A[lo], A[j]
    return j



def test_partition(A, val):
    idx = A.index(val)
    for i in range(idx, len(A)):
        if A[i] < val:
            return False
    return True

# A = [4, 1, 3, 0, 2, 5, 6]
# val = A[0]
# partition(A, 0, 6)
# print(A)
# partition(A, 0, len(A))
# print(test_partition(A, val))

def test():
    for _ in range(1000):
        A = list(range(20))
        import random as r
        r.shuffle(A)
        # A = [4, 1, 6, 0, 3, 7, 9, 8, 5, 2]
        old_A = list(A)
        # A = [4,3,2,1]
        val = A[0]
        partition(A, 0, len(A)-1)

        res = test_partition(A, val)
        if res == False:
            print("old", old_A)
            print("val", val)
            print("new", A)

# test()

# Test of partition is passed.

def quicksort(A, lo, hi):
    if lo < hi:
        idx = partition(A, lo, hi)
        quicksort(A, lo, idx - 1)
        quicksort(A, idx + 1, hi)

A = [3, 4, 2, 5, 0, 1, 1, 1, 1]
quicksort(A, 0, len(A) - 1)
# print(A)


# A = [3, 4, 2, 5, 0, 1, 1, 1, 1]
# A = [23,3,1,23,132,12,3,123,213,12,3]
import random as r
length = r.randint(1, 100)
A = [r.randint(1, 100) for _ in range(length)]

A_copy = list(A)
quicksort(A, 0, len(A) - 1)
A_copy.sort()
print(A == A_copy)
