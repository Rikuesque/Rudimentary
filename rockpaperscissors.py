import random
list = ["rock","scissors","paper"]
computer = random.choice(list)
while True:
    player = input("Choose your hand: ")
    print("Computer's hand: %s" % computer)
    if player.lower()=="rock":
        if computer=="scissors":
            print("You won!")
        elif computer=="paper":
            print("You lost!")
        elif computer=="rock":
            print("It's a tie!")
    elif player.lower()=="scissors":
        if computer=="rock":
            print("You lost!")
        elif computer=="scissors":
            print("It's a tie!")
        elif computer=="paper":
            print("You won!")
    elif player.lower()=="paper":
        if computer=="rock":
            print("You won!")
        elif computer=="scissors":
            print("You lost!")
        elif computer=="paper":
            print("It's a tie!")
            
    play = input('Enter "play" to play again: ')
    
    if play.lower() != "play":
        print("Game done.")
        break

