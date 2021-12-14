user = int(input("Enter an integer: "))

# def order(numbers):
#     numbers = sorted(numbers)
#     if user in numbers:
#         print("This number is in the list!")
#     else:
#         print("This number is not in the list...")
# order([1,3,5,9,6,17,346,7,235,55,107])

def search(numeros):
    first = 0
    last = len(numeros)-1
    middle = (last+first)//2
    while True:
        if user == numeros[middle]:
            print("%d is in the list!"% (user))
            break
        
        if first == last:
            print("%d is not on the list."% (user))
            break
        
        if user < numeros[middle]:
            last = middle-1
            middle = (last+first)//2
        elif user > numeros[middle]:
            first = middle+1
            middle = (last+first)//2
            
search(sorted([5]))   