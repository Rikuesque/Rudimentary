def number():
    return int(input("Enter a number: "))
numero = number()
condition = True

if numero == 1:
    condition = False
elif numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            condition = False
            break

if condition == False:
    print("%d is not a prime number."% numero)
else:
    print("%d is a prime number."% numero)
