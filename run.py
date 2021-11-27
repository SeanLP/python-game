import random

word = ['superman', 'batman', 'joker']

secret_word = random.choice(word)

display = []

GAME_OVER = False

# Replaces each letter in secret word with dashes
for letter in secret_word:
    display += '_'
print(display)

while not GAME_OVER:
    # Ask for user guess
    guess = input('Guess a letter: ').lower()

    # Check if guessed letter is in secret word
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    # Checks if there is no more dashes in secret word
    if '_' not in display:
        GAME_OVER = True
        print('Congratulations, you guessed the correct word and won!')