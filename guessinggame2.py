mid = 50
min = 0
max = 100
print("Choose a number between 1 and 100!")

while True:
    num = input("Is the number lesser, greater or equal to %d: "% mid)

    if num == "lesser":
        max = mid-1
        mid = (min+max)//2

    elif num == "greater":
        min = mid+1
        mid = (min+max)//2


    elif num == "equal":
        print("Bingo!")
        break
