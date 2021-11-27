import random

hangman_stages = ['''
    +------+
    |      |
    O      |
   /|\     |
   / \     |
           |
           |
       =========
''', '''
    +------+
    |      |
    O      |
   /|\     |
     \     |
           |
           |
       =========
''', '''
    +------+
    |      |
    O      |
   /|\     |
           |
           |
           |
       =========
''', '''
    +------+
    |      |
    O      |
    |\     |
           |
           |
           |
       =========
''', '''
    +------+
    |      |
    O      |
    |      |
           |
           |
           |
       =========
''', '''
    +------+
    |      |
    O      |
           |
           |
           |
           |
       =========
''', '''
    +------+
    |      |
           |
           |
           |
           |
           |
       =========
''']

word = ['superman', 'batman', 'joker']

secret_word = random.choice(word)

display = []

GAME_OVER = False

lives = 6

# Replaces each letter in secret word with dashes
for letter in secret_word:
    display += '_'
print(f"{' '.join(display)}")

while not GAME_OVER:
    # Ask for user guess
    guess = input('Guess a letter: ').lower()

    # Check if guessed letter is in secret word
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in secret_word:
        lives -= 1
        if lives == 0:
            GAME_OVER = True
            print(f'Hard luck, you lost, the word was {secret_word}')

    print(f"{' '.join(display)}")

    # Checks if there is no more dashes in secret word
    if '_' not in display:
        GAME_OVER = True
        print('Congratulations, you guessed the correct word and won!')

