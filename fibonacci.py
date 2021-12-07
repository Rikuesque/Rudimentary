number = int(input("How may Fibonacci numbers: "))
def sequence():
    list = [1]
    a, b = 0, 1
    for i in range(number):
        a, b = b, a+b
        list.append(b)
    print(list)
        
sequence()
