import random
rando = str(random.randint(1000, 9999))
count = 0
# print(rando)

# def checker():
while True:
    count += 1
    cows = 0
    bulls = 0
    user = input("Enter a four digit number: ")
    for index,item in enumerate(user):
        if item in rando:
            if rando[index] == item:
                cows +=1
            else:
                bulls +=1
    print(cows, bulls)
    if cows == 4:
        break
print("The answer was %s, you took %d tries." % (rando, count))
# checker()