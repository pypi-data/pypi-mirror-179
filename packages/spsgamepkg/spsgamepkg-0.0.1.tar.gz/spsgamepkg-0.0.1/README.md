Rock Paper Scissors - a basic program to play rock,paper,scissors with PC
=========================================================================

# A fun Python package to play rock paper scissors with PC
This is just a basic stress-buster game module to play with your PC
Created by Aswin Venkat <aswinvenk8@gmail.com>

Installation
============

Run the following to install:

```python
pip install stonepaperscissorsgamepkg
```

Methods
=======

1. game.rules()
    Will display the rules of the game

2. game.Game('name').game(count:int)
    Count -> The number of times you want to play the game with PC

3. game.Game('name').clear_score()
    Will clear the score (initialise the score back to 0)

4. game.Game('name').display_result()
    Will display the result of the game.

5. game.Game('name').condition(pc='', player='')
    entering ['stone' or 'paper' or 'scissors'] in pc='{}' and player='{}' will directly give you the result

EXAMPLE CODE
============

```python
from src.spsgamepkg import game

# Display rules
>> game.rules()

# initialize player
aswin_game=game.Game('Aswin')

# Play a game
>> aswin_game.game(5)

# Display Result
>> aswin_game.display_result()

# Reset the scores
>> aswin_game.clear_score()
```