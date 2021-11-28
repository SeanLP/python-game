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

  
* **Input**

    * Input validation.

    * You cannot enter a string.

    * You cannot enter a number.

    * You cannot enter the same guess.

![String-warning](https://seanlp.github.io/python-game/assets/images/string.png)

![Number-warning](https://seanlp.github.io/python-game/assets/images/number.png)

![Same-warning](https://seanlp.github.io/python-game/assets/images/same-letter.png)

* **Future Features**

    * Create different categories of words for user to choose from.

    * Alter game difficulty by decreasing starting lives.

## Testing
---
* Passed the code through a PEP8 linter and confirmed there are no problems.

* Let the user know if they give an invalid input such as a string or number.

* Tested in my local terminal and the Code Institute Heroku terminal.

## Bugs
---
* I was getting an error on the user guess because i forgot to add the .lower() method to the input.

## Remaining Bugs
---
* No bugs remaining.

## Validator Testing
---
* No errors were returned from PEP8online.com

## Deployment
---
* This project was deployed using Code Institute's mock terminal for Heroku.

* Fork or clone this repository.

* Create a new Heroku app.

* Set the buildpacks to Python and NodeJS in that order.

* Link the Heroku app to the repository.

* Click on Deploy.

## Credits
---
* Code Institute for the deployment terminal.

* Wikipedia for the details of the Hangman game.

* Code for logo from [Ascii](https://ascii.co.uk/art/hangman)

* Some code was used from [YouTube](https://www.youtube.com/watch?v=wmSysRui0cI&t=308s)