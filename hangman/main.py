import random
import hangman_art

print(hangman_art.logo)
from hangman_words import word_list

lives = 6



chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    display = ""
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess in chosen_word:
        print(f'You guessed "{guess}"')
    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed "{guess}", which was not in the word. You lose a life!')
        if lives == 0:
            game_over = True


            print(f'*********************** IT WAS "{chosen_word}" YOU LOSE**********************')


    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    from hangman_art import stages
    print(stages[lives])
