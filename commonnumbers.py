import random
a = [random.randrange(1,15) for i in range(0,20)]
print(a)
b = [random.randrange(1,20) for i in range(0,15)]
print(b)
newList = []
for x in a:
    for y in b:
        if x == y:
            if not x in newList:
                newList.append(x)
print(newList)
