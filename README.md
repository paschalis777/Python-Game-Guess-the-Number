# Python-Game-Guess-the-Number
The provided Python application is a simple number guessing game created using the Tkinter library. Here's a description of what the application does:

1. **Game Objective**: The application's objective is for the player to guess a randomly generated number between 1 and 100.

2. **User Interface**: It provides a graphical user interface (GUI) with the following elements:
   - A label that explains the game's objective.
   - An entry field for the player to input their guess.
   - A "Check" button to submit the guess.
   - A "Clear" button to clear the input field.
   - A "New Game" button to start a new game.
   - A label that displays the result of the guess.
   - A label that shows the remaining number of attempts.

3. **Game Logic**:
   - The game starts with a hidden number randomly generated between 1 and 100.
   - The player has a limited number of attempts (default: 10) to guess the correct number.
   - After each guess, the application provides feedback:
     - If the guess is correct, it displays a victory message and the number of attempts.
     - If the guess is too low, it prompts the player to try a higher number.
     - If the guess is too high, it prompts the player to try a lower number.
   - If the player runs out of attempts without guessing the correct number, the game ends, and the correct number is revealed.

4. **Extra Features**:
   - The "Enter" key can also be used to submit a guess.
   - The "Clear" button allows the player to clear the input field.
   - A trophy image is displayed in a separate window when the player wins the game.

5. **New Game**:
   - The "New Game" button allows the player to start a new game with a new random number.

In summary, the application provides a fun number guessing game where the player's objective is to guess the hidden number within a limited number of attempts.
It offers an interactive GUI and provides feedback on each guess. When the game is won, a trophy image is displayed to celebrate the victory.
