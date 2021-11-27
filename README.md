# Hanngman Game

Hangman is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Users try to beat the computer by guessing the letters in the secret word before they run out of lives.

[Here is the live version of my project](https://python-hangman-ci.herokuapp.com/)

![Responsive-Website](https://seanlp.github.io/python-game/assets/images/hangman.png)

## How to play
---

This hangman game is based on the classic pen and paper game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game))

In this version, the computer randomly chooses a word for the user to guess and hides the letters with dashes.

The user is then prompted to guess the word and can see how many letters are in it.

If the user correctly guesses the letter it will appear in the word replacing the dash symbol.

If the user's guess is wrong the hangman image will show on the terminal, and any more subsequent wrong guesses will cause the hangman image to fill in and the user loses.

The user wins if they correctly guessed each letter in the secret word while still retaining any lives.

## Features
---
* **Existing Features**

    * Random word generation.

    * The random word's letters are replaced with dash symbols.

    * At the start, the user cannot see the word but can see how many letters it contains.

    * Accepts user input.

![Game-start](https://seanlp.github.io/python-game/assets/images/game-start.png)