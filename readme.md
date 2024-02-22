## Turtle Crossing Game - 100 days of python

This is a simple game built using the Turtle module in Python, where the player (represented by a turtle) tries to cross a busy road without getting hit by cars.

### Components

#### main.py
This is the main file of the game. It sets up the screen, initializes the player, scoreboard, and car manager. The game loop runs continuously, updating the screen, generating cars, moving cars, detecting player progress, and collisions.

#### player.py
Defines the Player class, which represents the player turtle. It handles the movement of the player and resetting the player's position.

#### car_manager.py
Contains the CarManager class, responsible for managing the cars in the game. It generates cars, moves them, and increases their speed as the game progresses.

#### scoreboard.py
Implements the Scoreboard class, which displays the current level of the game. It also handles updating the level and displaying the game over message.

### How to Play

- Use the up arrow key to move the player turtle forward.
- Avoid colliding with the cars moving horizontally across the screen.
- Reach the top of the screen to advance to the next level.
- The game ends if the player collides with a car.

### Dependencies

- Python 3.x
- Turtle module

### Running the Game

1. Make sure you have Python installed on your system.
2. Run the `main.py` file.
3. Use the up arrow key to move the player turtle.
4. Have fun trying to cross the road without getting hit!

### Customization

You can customize various parameters of the game, such as starting move distance, colors, and speeds, by modifying the constants defined in the code files.