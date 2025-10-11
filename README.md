# Overview

This project is a classic **Snake Game** built with Python and PyGame.  
My goal in creating it was to strengthen my understanding of game loops, event handling, collision detection, and rendering using the PyGame library. By developing this game, I practiced managing real-time input, updating game state logic, and creating an interactive user experience.

The game follows the traditional _Snake_ gameplay mechanics — the player controls a growing snake that moves across the screen to eat fruit while avoiding collisions with the walls or itself.

### How to Play

- Use the **arrow keys** to move the snake up, down, left, or right.
- Each time the snake eats a fruit, it grows longer and your score increases.
- The game ends if the snake collides with itself or the screen boundaries.
- Try to achieve the highest possible score before crashing!

The game uses a simple and responsive control system, along with an image-based fruit for a polished look.

### Purpose

The purpose of developing this software is to deepen my practical understanding of **game development with Python**, focusing on:

- Managing continuous loops and frame updates.
- Handling user input and event-driven logic.
- Applying collision detection and sprite rendering.
- Structuring clean, maintainable, and scalable Python code.

# Development Environment

- **IDE:** Visual Studio Code
- **Language:** Python 3.10
- **Libraries:**
  - `pygame==2.6.1` – for graphics, input, and sound
  - `random` – to randomly place fruit on the board
  - `sys` – for exiting the game cleanly

I developed and tested the game in a virtual environment (`venv`) to keep dependencies isolated and ensure consistent behavior across systems.

# Useful Websites

- [PyGame Docs](https://www.pygame.org/docs/)
- [PyGame Tutorial Video](https://www.youtube.com/watch?v=8OMghdHP-zs)
- [RGB color palletes](https://www.rapidtables.com/web/color/RGB_Color.html)

# Future Work

There are several improvements and new features I plan to add to enhance the gameplay experience and visual quality:

- **Add more complex graphics for the snake** – Currently, the snake is drawn using simple rectangles. In the future, I plan to design or import custom sprite images for the snake’s head, body, and tail to make the visuals more dynamic and engaging.
- **Improve the fruit bite sound effect** – There’s currently about a 2-second delay when playing the sound after eating a fruit. I intend to optimize sound loading and playback timing for a more responsive experience.
- **Implement a main menu and pause functionality** – Adding a start menu, pause feature, and game-over screen will make the game feel more complete and user-friendly.
- **Add score persistence** – Save the highest scores locally or to a file, allowing players to track progress across sessions.
- **Introduce increasing difficulty** – Gradually increase snake speed as the score grows to make the game more challenging over time.
- **Polish UI elements** – Add a cleaner score display, background, and possibly a restart button for a smoother gameplay loop.
