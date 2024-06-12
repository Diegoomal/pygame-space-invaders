# Space Invaders in Pygame

This repository contains a classic 2D Space Invaders game implemented using the Pygame library. The game is designed to provide a fun, nostalgic experience with simple controls and engaging gameplay. The project follows an object-oriented approach to ensure the code is modular and easy to maintain.

## Features
- Classic Space Invaders Gameplay: Shoot down waves of enemies while avoiding their attacks.
- Object-Oriented Design: The game is implemented using object-oriented principles, making it easy to extend and maintain.
- Customizable Settings: Easily modify game settings such as screen dimensions, colors, speeds, and more.
- Score Display: Real-time score display to track your progress.
- Accurate Collision Detection: Detects collisions between bullets and enemies for realistic gameplay.
- Configurable Environment: Separate configuration file for easy customization of game settings.

## Project Structure
- main.py: The main file that initializes the game, handles the game loop, and manages user inputs.
- player.py: Defines the Player class, responsible for the player’s attributes, movements, and shooting.
- enemy.py: Defines the Enemy class, responsible for enemy attributes and movements.
- bullet.py: Defines the Bullet class, responsible for the bullets fired by the player.
- environment.py: Defines the GameEnvironment class, responsible for drawing the game environment and displaying the score.
- config.py: Contains all configurable settings for the game, such as screen dimensions, colors, and speeds.

## Execute

Create CONDA env
```
conda env create -n space-invaders-env -f ./env.yml
```

Activate CONDA env
```
conda activate space-invaders-env
```

Execute game
```
python src/main.py
```

## Customization
You can customize the game settings by modifying the config.py file. This includes changing the screen width and height, colors, paddle and ball speeds, and more.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acnowledgements
This project is built using the Pygame library. Inspired by the original Pong game created by Atari. Enjoy the game!

## URL
[github](https://github.com/Diegoomal)