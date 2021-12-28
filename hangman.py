import random
words = []

with open('Dictionary.txt', 'r') as w:
    while w.readline().strip():
        words.append(w.readline().strip())
word = list(random.choice(words))
answer = ''.join(word)
correct = list("_" * len(word))
guessed = []
wrong = 0
print(word)

while True:
    guess = input("Choose a letter: ").upper()
    if guess in word:
        while guess in word:
            index = word.index(guess)
            correct[index] = guess
            word[index] = 0
            if guess not in word:
                print("That letter is correct.", correct)
                guessed.append(guess)
                break
    elif guess in guessed:
        print("You already tried that word.")
    elif guess not in word:
        print("Your guess is not in the word.")
        guessed.append(guess)
        wrong+=1
        print("You have %d chances left." % (6-wrong))
    if ''.join(correct) == answer:
        print("You guessed the word!")
        break
    elif wrong == 6:
        print("You lost the game.")
        break