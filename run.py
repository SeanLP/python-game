# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
# randomly selects game word froma list of words

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
print(HANGMAN_STAGES[6])
