import random

word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)
play = True
lives = 6

print(f'Pssst, the solution is {word}.')
display = []
for w in word:
    display.append("_")


while play:
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
        
    print(f"{' '.join(display)}")
    print(stages[lives])
    
    if lives == 0:
        print("You Lose")
        play = False

    if "_" not in display:
        print("You Win")
        play = False
