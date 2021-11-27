import random

word = ['superman', 'batman', 'joker']

secret_word = random.choice(word)

display = []

for letter in secret_word:
    display += '_'
print(display)

guess = input('Guess a letter: ').lower()

for position in range(len(secret_word)):
    letter = secret_word[position]
    if letter == guess:
        display[position] = letter

print(display)