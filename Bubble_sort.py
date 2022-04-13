import random

lst = list()
for n in range(100):
    lst.append(random.randint(0,100))

print(lst)

for x in range(len(lst)-1):
    for y in range(len(lst)-1-x):
        if lst[y] > lst[y+1]:
            tmp = lst[y]
            lst[y] = lst[y+1]
            lst[y+1] = tmp

print(lst)
