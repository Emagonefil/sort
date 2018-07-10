
#use two array


def sort(c):
    if len(c) == 1:
        return c
    else:
        mid_idx = len(c)//2
        
        left = c[:mid_idx]
        right = c[mid_idx:]       
        return merge(sort(left), sort(right))

    

def merge(a, b):
    c, i = [], 0
    while len(a) != 0 and len(b) != 0:
        print(i)
        if a[i] < b[i]:
          c.append(a[i])
          a.remove(a[i])
        else:
          c.append(b[i])
          b.remove(b[i])
    if len(a) == 0 or len(b)== 0:
        c = c + a + b       
    return c


def test_merge():
  assert merge([1, 3, 10], [2, 4, 8, 11]) == [1, 2, 3, 4, 8, 10, 11]
  assert merge([2, 4, 8, 11], [1, 3, 10]) == [1, 2, 3, 4, 8, 10, 11]
  assert merge([1, 3], [2, 4]) == [1, 2, 3, 4]
  assert merge([1], [2]) == [1, 2]
  assert merge([2], [1]) == [1, 2]
  assert merge([1], []) == [1]
  assert merge([], [2]) == [2]
  assert merge([], []) == []
  print("test_merge() passed")



def test_sort():
  import random as r
  for _ in range(100):
    l = [i for i in range(100)]
    r.shuffle(l)
    assert sort(l) == [i for i in range(100)]
  print("test_sort() passed")
    
test_sort()
test_merge()

list1 = [45, 5, 0, 12, 7, 9, 37, 1]
print(list1)
print(sort(list1))

