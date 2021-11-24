import random
import time

HANGMAN_STAGES = ['''
    +-----+
    |     |
          |
          |
          |
          |
        ------ ''', '''
    +-----+
    |     |
    O     |
          |
          |
          |
        ------ ''', '''
    +-----+
    |     |
    O     |
    |     |
          |
          |
        ------ ''', '''
    +-----+
    |     |
    O     |
   /|     |
          |
          |
        ------ ''', '''
    +-----+
    |     |
    O     |
   /|\    |
          |
          |
        ------ ''', '''
    +-----+
    |     |
    O     |
   /|\    |
   /      |
          |
        ------ ''', '''
    +-----+
    |     |
    O     |
   /|\    |
   / \    |
          |
        ------ ''']

superHeroes = ['batman', 'superman', 'wonderwoman', 'aquaman', 'flash',
               'darkseid', 'galactus', 'joker', 'bane', 'robin', 'thor',
               'ironman', 'hulk', 'hawkeye', 'mystique', 'spiderman',
               'thanos', 'deadpool']

tolkienCharacters = ['frodo', 'bilbo', 'sam', 'merry', 'pippin',
                     'gandalf', 'saruman', 'sauron', 'aragorn',
                     'legolas', 'gimli', 'borimir', 'faramir',
                     'gollum', 'shelob', 'balrog', 'lurtz']

name = input("Please enter your name ")
print("Hello", name.capitalize(), "let's play Hangman!")
time.sleep(.5)
print("To win you must guess the secret word chosen by the computer.")
time.sleep(.5)
print("You can only guess one letter at a time,") 
print("if you guess the wrong letter, the man will start to hang!")
time.sleep(1)
print("Let's play Hangman!")
