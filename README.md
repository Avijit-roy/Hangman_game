# Hangman Game

A classic word-guessing game built in Python. Test your vocabulary and deduction skills as you try to guess the hidden word before running out of attempts.

## Features

- **Classic Gameplay**: Traditional hangman rules and mechanics
- **Random Word Selection**: Different words each game for varied challenges
- **Simple Interface**: Command-line based gameplay for easy interaction
- **Attempt Tracking**: Monitor your remaining guesses as you play
- **Word Validation**: Smart letter guessing with feedback

## Installation

### Prerequisites

- Python 3.x
- Git (for cloning the repository)

### Setup Instructions

Follow these steps to get the game running on your system:

```bash
# 1. Install Python 3
apt install python3

# 2. Install Git
apt install git

# 3. Clone the repository
git clone https://github.com/Avijit-roy/Hangman_game.git

# 4. Navigate to the project directory
cd Hangman_game

# 5. Run the game
python3 hangman_game.py
```

## How to Play

1. Run the game using the command above
2. The game will display blanks representing each letter in the hidden word
3. Guess one letter at a time
4. Correct guesses reveal letters in the word
5. Incorrect guesses reduce your remaining attempts
6. Win by guessing all letters before running out of attempts
7. Game over if you exhaust all your attempts without solving the word

## Technologies Used

- **Python 3**: Core game logic and functionality
- **File Structure**:
  - `hangman_game.py`: Main game script with game logic
  - `randomdfv.py`: Word selection and randomization module

## File Structure

```
├── hangman_game.py   # Main game script
├── randomdfv.py      # Word selection module
├── LICENSE           # MIT License
├── README.md         # This file
└── .gitattributes    # Git configuration
```

## Requirements

- Python 3.x installed on your system
- Linux/Unix/Mac/Windows terminal access

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Avijit Roy**

---

*Challenge your mind with the classic word-guessing game. Can you solve the hangman before time runs out?*
