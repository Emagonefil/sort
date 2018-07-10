# Insertion sort

def ins_sort(l):
  for i in range(1, len(l)):  # (1) N-1
    j = i                     # (2)
    # (3) i-1 (worst case)
    while ((j - 1) >= 0) and l[j] < l[j-1]:
      l[j], l[j-1] = l[j-1], l[j]
      j = j - 1

# [1, 3, 5, 7, 6, 4, 2]
# => [1, 2, 3, 4, 5, 6, 7]
a = [1, 3, 5, 7, 6, 4, 2]
ins_sort(a)
print(a)

# speed?    (n-1)*(n-1)/2 = O(n^2)
# in-place? yes
# stable?   
