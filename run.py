import random

hangman_stages = ['''
    +------+
    |      |
           |
           |
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
    |\     |
           |
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
   / \     |
           |
           |
       =========
''']

word = ['superman', 'batman', 'joker', 'spiderman', 'wonderwoman', 'thor',
        'hulk', 'daredevil', 'wolverine', 'aquaman', 'flash', 'deadpool',
        'supergirl', 'antman', 'atom', 'batgirl', 'batwoman', 'catwoman',
        'elektra', 'hawkeye', 'hellboy', 'ironman', 'marvelman', 'robin',
        'wasp', 'watchmen', 'thanos', 'magneto', 'loki', 'darkseid',
        'galactus', 'brainiac', 'doomsday', 'apocalypse', 'ultron',
        'kingpin', 'scarecrow', 'deathstroke', 'venom', 'carnage',
        'bane', 'bizarro', 'sinestro', 'mystique', 'deadshot', 'bullseye',
        'zoom', 'penguin', 'abomination', 'dormammu', 'hobgoblin', 'riddler',
        'lizard', 'sandman', 'clayface', 'mysterio', 'electro', 'morbius']

secret_word = random.choice(word)

display = []

GAME_OVER = False

lives = 0

# Replaces each letter in secret word with dashes
for letter in secret_word:
    display += '_'
print(f"{' '.join(display)}")
print()

while not GAME_OVER:
    # Ask for user guess
    guess = input('Guess a letter: ').lower()

    # Check if guessed letter is in secret word
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display[position] = letter

    # If guess is incorrect, user's lives increase by 1, if 6 game ends
    if guess not in secret_word:
        lives += 1
        if lives == 6:
            GAME_OVER = True
            print(f'Hard luck, you lost, the word was {secret_word}')

    print(f"{' '.join(display)}")

    # Checks if there is no more dashes in secret word
    if '_' not in display:
        GAME_OVER = True
        print('Congratulations, you guessed the correct word and won!')

    # Displays current hangman stage    
    print(hangman_stages[lives])
