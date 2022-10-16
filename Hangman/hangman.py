
lives = 6
Game_over = False
#step 1 :- Generate a random word
import random

word_list = [
    'HyperTextMarkupLink', 'CascadingStyleSheets', 'Python', 'Java', 'JavaScript', 'Swift', 'C++', 'C#', 'R',
    'Golang', 'PHP', 'TypeScript', 'Scala', 'Shell', 'PowerShell', 'Perl',
    'Haskell', 'Kotlin', 'VisualBasicNET', 'StructuredQueryLanguage', 'Delphi',
    'MATLAB', 'Groovy', 'Lua', 'Rust', 'Ruby'
]

chosen_word = random.choice(word_list).lower()
print(chosen_word)
#Step 2:- Generate blanks
display = list()
for i in range(0, len(chosen_word)):
    display.append('_')
#print(' '.join(display))

while not Game_over:
    #Step 3:- Ask user to guess a letter
    guess = input("Select a letter \n")

    #Step 4:-Is the guessed letter in the word_list
    for position in range(0, len(display)):
        if guess == chosen_word[position]:
            #Step 5:-Replace the blank with the letter
            display[position] = guess
    #Step 6:-Lose a life
    if guess not in chosen_word:
        lives -= 1
        #Step 7:- Have they run out of lives
        if lives == 0:
            print("you lose")
            print()
            Game_over = True

    print(' '.join(display))
    #Step 8:- Are all the blanks filled
    if "_" not in display:
        print("You Win")
        Game_over = True
    print(stages[lives])
#Step 9:- Game Over
print("Game over")
