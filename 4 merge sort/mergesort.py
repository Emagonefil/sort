def merge(a, b):  # not in-place, O(N)
  c, i, j = [], 0, 0
  while i < len(a) and j < len(b):
    if a[i] < b[j]:
      c.append(a[i])
      i += 1
    else:
      c.append(b[j])
      j += 1
  c = c + a[i:] + b[j:]
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
  
test_merge()

def mergesort(l):
  if len(l) == 1:           # recursion termination
    return l
  else:
    mid_idx = len(l) // 2   # find middle index
    left = l[:mid_idx]
    right = l[mid_idx:]
    return merge(mergesort(left), mergesort(right)) # recursion

def test_mergesort():
  import random as r
  for _ in range(100):
    l = [i for i in range(100)]
    r.shuffle(l)
    assert mergesort(l) == [i for i in range(100)]
  print("test_mergesort() passed")
    
test_mergesort()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
