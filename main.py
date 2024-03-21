import random
import hangman_art
import hangman_words

print(hangman_art.logo)
word_list = hangman_words.word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = ['_' for _ in chosen_word]
print(' '.join(display))

lifeline = 6  # Set the number of allowed wrong guesses

while lifeline > 0:
    guess = input("Guess a Letter: ").lower()
    found = False

    if guess in display:
        print(f"You've already guessed the letter '{guess}'. Try another one.")
        continue

    for i in range(word_length):
        if chosen_word[i] == guess:
            display[i] = guess
            found = True

    if not found:
        lifeline -= 1
        print("Wrong guess. You lost a life.")

    print(' '.join(display))

    if '_' not in display:
        print("Congratulations! You've guessed the word:", chosen_word)
        break

    print(f"Lifelines left: {lifeline}")
    print(hangman_art.stages[lifeline])

if lifeline == 0:
    print("Oops! You've run out of lifelines. The word was:", chosen_word," You loose the game")
    print(hangman_art.stages[lifeline])
