import random
from time import sleep

logo = '''
 _                                              
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ '''

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

game_over = False

lives = 0

print(logo)
print()
print('Welcome to Hangman, SuperHero Edition!')
sleep(2)
print('Rules: Guess a letter, one at a time, to see if its in the secret word')
print('If you guess wrong, you lose a life and the man will start to hang')
print()
sleep(1)
# Replaces each letter in secret word with dashes
for letter in secret_word:
    display += '_'
print(f"{' '.join(display)}")
print()

while not game_over:
    # Ask for user guess
    guess = input('Guess a letter: ').lower()

    # Checks if user already guessed letter
    if guess in display:
        print(f'You already guessed {guess}')

    # Check if guessed letter is in secret word
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display[position] = letter

    # If guess is incorrect, user's lives increase by 1, if 6 game ends
    if guess not in secret_word:
        print(f"You guessed {guess}, that's not in the word")
        lives += 1
        if lives == 6:
            game_over = True
            print(f'Hard luck, you lost, the word was {secret_word}')
        # Guess can't be more than one letter
        elif len(guess) != 1:
            print('Please enter a Single Letter')
        # Guess can't be a number
        elif guess.isdigit():
            print('Please enter a Letter')
    
    print(f"{' '.join(display)}")

    if '_' not in display:
        game_over = True
        print('Congratulations, you guessed the correct word and won!')

    # Displays current hangman stage    
    print(hangman_stages[lives])
