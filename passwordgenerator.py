import random
length = int(input("Enter an integer for the password length: "))
everything = list("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.?!$#@%&")
def generator():
    print("".join(random.choices(everything, k=length)))
    
generator()
