number = int(input("How may Fibonacci numbers: "))
def sequence():
    a, b = 0, 1
    list = []
    if number == 0:
        list = []
    elif number == 1:
        list = [1]
    elif number == 2:
        list = [1, 1]
    elif number > 2:
        list = [1]
        for i in range(number-1):
            a, b = b, a+b
            list.append(b)
    print(list)
        
sequence()
