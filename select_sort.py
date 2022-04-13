import random
rada  = [x for x in range(100,0,-1)]
lst = []
while len(rada) != 0:
    x = random.randint(0,len(rada)-1)
    lst.append(rada[x])
    rada.pop(x)
print(lst)


for i in range(len(lst)):
    vrh = i
    for j in range(i,len(lst)):
        if lst[vrh] < lst[j]:
            vrh = j
    tmp = lst[i]
    lst[i] = lst[vrh]
    lst[vrh] = tmp
print(lst)
print(lst == [x for x in range(100,0,-1)])
