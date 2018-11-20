# Othello Project

This project aims to develop an interactive Othello Game with Python and processing. The classes used in this project is listed as follows

- Tile: represents a single tile object

- Tiles: a collection of Tile object

- Board: represents the board object

- Player: the player object

- AI: Inherited from the Player class, adopts its own strategy to make a move each turn. Strategies applied are as follows

   - greedy strategy: place the tile at the position which leads to the most flips
   - corner strategy: takes up the corner position 
   - block strategy: make a move such that the opponent player cannot make a move the next turn, if possible

- GameController: controls the shift of the human player and AI, also receives legal mouse press

  