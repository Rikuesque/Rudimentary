import random
count = 0
numero = random.randint(1,9)
while True:
    guess = int(input("Guess a random integer: "))
    count += 1
    if guess < numero:
        print("Your guess was too low!")
    elif guess > numero:
        print("Your guess was too high!")
    else:
        print("Bingo! You took %d guesses."% count)
        play = input('Enter "exit" to quit: ')
        if play.lower() == "exit":
            print("Game done.")
            break
        else:
            numero = random.randint(1,9)
            count = 0
            None
