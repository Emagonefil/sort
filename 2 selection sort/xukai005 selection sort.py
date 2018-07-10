# Selection sort

# In-place

def my_min(l):
  v = l[0]
  # for n in l:
    # if n < v:
      # v = n
  for i in range(len(l)): # n => l[i]
    if l[i] < v:
      v = l[i]
  return v

def argmin(l):
  v = l[0]
  idx = 0
  for i in range(len(l)): # 0 ~ l-1
    if l[i] < v:
      v = l[i]
      idx = i
  return idx

print(argmin([1,3,2]))
# => 0

def select_sort(l):
  # (1) i = 0 ~ l-1
  for i in range(0, len(l)-1):
    # (2) idx = argmin(l(i~end))
    v = l[i]
    j = i
    for idx in range(i, len(l)): # i ~ l-1
      if l[idx] < v:  # comparison happens here
        v = l[idx]
        j = idx
    # (3) swap l[i] and l[j]
    l[i], l[j] = l[j], l[i]
  return l

print(select_sort([1,3,2,4,7,6,5]))
# => [1,2,3,4,5,6,7]

l = [1,3,2,4]
select_sort(l)
print(l)

# Not in-place

def select_sort2(l):
  old_l = list(l)         # copy the input list
  new_l = []              # create an empty list
  while len(old_l) > 0:   # do while there is number
    m = min(old_l)        # find the minimum value left
    new_l.append(m)       # add the minimum value to the new list
    idx = old_l.index(m)  # remove the minimum value (1. find the index of the minimum value)
    old_l.pop(idx)        # remove the minimum value (2. remove it using pop())
  return new_l            # return the new list

print(select_sort2([1,3,2,4,7,6,5]))
# => [1,2,3,4,5,6,7]

l = [1,3,2,4]
select_sort2(l)
print(select_sort2(l))
print(l)
