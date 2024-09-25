# simple-snake-game
Here’s a README file tailored to your Snake Game written in Python using the `turtle` module:


# Snake Game

## Overview

This is a classic **Snake Game** implemented in Python using the `turtle` graphics library. The objective of the game is to control the snake, eat food, and grow as long as possible without colliding with the walls or the snake's own body. The game runs in a graphical window and tracks both your score and high score.

## Features

- **Simple Gameplay**: Control the snake with arrow keys to move up, down, left, and right.
- **Score System**: Earn points by eating food, and try to beat your high score.
- **Game Over Condition**: The game ends when the snake hits the wall or its own body.
- **Real-time Rendering**: Game rendered using the `turtle` module for simple graphics.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- **Python 3.x** installed. You can download it from [here](https://www.python.org/downloads/).
- `turtle` graphics library is pre-installed with Python, so no additional installations are necessary.


### Run the Game

Once you've obtained the game file (`game.py`), follow these steps to run it:

1. Open a terminal or command prompt.
2. Navigate to the directory where the `game.py` file is located.
3. Run the game with the following command:
   ```bash
   python game.py
   ```

## How to Play

- **Objective**: Control the snake to eat the food that randomly appears on the screen and grow in length. Avoid hitting the walls or colliding with the snake's own body.
- **Controls**: Use the arrow keys to move the snake:
  - **Up Arrow**: Move the snake upward.
  - **Down Arrow**: Move the snake downward.
  - **Left Arrow**: Move the snake left.
  - **Right Arrow**: Move the snake right.
  
- **Scoring**: Each time the snake eats food, your score increases by 10 points. If you beat your previous high score, it will be updated and displayed on the screen.

## Game Flow

1. **Starting**: The snake starts in the center of the screen and can be controlled with the arrow keys.
2. **Eating Food**: When the snake reaches the food, its length increases, and a new piece of food appears at a random location.
3. **Game Over**: The game ends if the snake hits the walls or itself. The current score and high score will be displayed, and the game can be restarted.

### Example Gameplay

```
Score: 0     High Score: 50

- Use arrow keys to control the snake.
- Eat food (white circle) to grow and score points.
- Avoid hitting the walls and your own tail.
```

## Customization

You can modify the game to add more features or change the behavior:

- **Change Snake Speed**: Modify the `delay` variable to increase or decrease the snake's speed.
- **Add Obstacles**: You can add static obstacles to make the game more challenging.
- **Change Snake Appearance**: Modify the shape and color of the snake by changing the parameters in the `turtle.Turtle()` object.

Example for changing snake speed:
```python
delay = 0.05  # Faster snake
```

## Known Issues

- **Collision Detection**: The game might not detect collisions perfectly if the snake moves too fast. Adjusting the `delay` value can improve the accuracy of collision detection.
- **Pen Error**: Ensure that the line `pen = turtle.Turtle()` is corrected since the current code uses `pen = turtle.Turtle`, which may cause issues.

