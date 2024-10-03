# Two Squares Game

## Overview

The **Two Squares Game** is a simple, turn-based game where two players take turns selecting two numbers from a 4x4 board (numbers 1 to 16). The goal is to form a vertical or horizontal rectangle by choosing two adjacent numbers. A number on the board cannot be selected twice, and the game ends when no valid moves remain. The player who places the last valid pair wins the game!

## Features

- **Two-player turn-based gameplay**: Players alternate turns, selecting pairs of numbers to form rectangles.
- **4x4 Board**: A 4x4 board (numbers 1 to 16) is displayed, updated after each turn.
- **Valid move checking**: The game ensures that selected numbers form either a vertical or horizontal rectangle.
- **Win condition**: The last player who can place a valid pair of numbers wins the game.
- **Input validation**: The game only accepts valid, unused numbers as inputs from both players.
  
## Rules of the Game

1. **Board Setup**: The game starts with a 4x4 board containing numbers from 1 to 16, arranged in rows and columns.
   
2. **Player Turn**: 
    - Player 1 starts by choosing two adjacent numbers, either horizontally or vertically. 
    - Player 2 follows with their turn, selecting another valid pair of adjacent numbers.

3. **Valid Moves**: 
    - Players must choose two numbers that form a rectangle, meaning they are adjacent either horizontally or vertically.
    - Once selected, the numbers are removed from the board and marked with an 'X' to indicate they are no longer available.

4. **Winning the Game**: 
    - The game continues until no more valid moves can be made.
    - The player who makes the last valid move wins the game.

## How to Play

1. Clone or download this repository to your local machine.
   
2. Run the game by executing the Python script:

    ```bash
    python two_squares_game.py
    ```

3. Follow the prompts in the console to select numbers:
    - Player 1 and Player 2 will take turns selecting two numbers.
    - The game will display the updated board after each turn.
    - The first player to complete the game with the last valid move wins!

## Example

```bash
Welcome to two squares game
The last player who can place a card on the board is the winner.

******************************
||  1  ||  2  ||  3  ||  4  ||
||  5  ||  6  ||  7  ||  8  ||
||  9  || 10  || 11  || 12  ||
|| 13  || 14  || 15  || 16  ||
******************************

Player1, please choose the first number from 1 to 16: 1
Player1, please choose the second number from 1 to 16: 2
