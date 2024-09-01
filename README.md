# Dice Simulation

## Description
A simple dice stimulation that rolls a die or 2 dice for one player.

## Installation
To set up and run the Dice Simulation game on your local machine, follow these steps:

### 1. Clone the Repository
First, clone the repository to your local machine. Open a terminal and run:
```bash
git clone https://github.com/MilaniTetani/Dice-Simulation.git
```
### 2. Navigate to the Project Directory
Change to the project directory:
```bash
cd Dice-Simulation
```
### 3. Set Up a Virtual Environment (if not already set up)
If you do not have a virtual environment already set up, create and activate one:
On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
### 4. Activate the Existing Virtual Environment
If the venv folder already exists and contains the necessary packages, activate it:
On Windows:
```bash
venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```
### 5. Running the Script
To run the script, use the terminal within your project directory:
```bash
python dice_simulation.py
```
### 6. Note on PIL Imports
Ensure that:
- The virtual environment is activated before running the script.
- The 'Pillow' library is installed in the virtual environment.
### 7. Troubleshooting
If you face any issues, make sure to:
- Check the Python interpreter settings in VS Code to ensure it points to the virtual environment's interpreter.
- Verify that the virtual environment contains all necessary packages by running pip list and checking for 'Pillow' in the output.

## Features
- Roll a single die
- Roll two dice
- Option to switch between rolling one die and two dice
- Option to continue playing or stop

## Future Fetures
Below are some of the planned enchancements for the Dice Simulation project:

1. Track Results
    - Branch: 'track-results'
    - Description: Add functionality to track and display the results of each roll session.
      
2. Statistics and Analytics
    - Branch: 'statistics'
    - Description: Implement features to calculate and display statistics such as the frequency of each number rolled.
      
3. User Customization
    - Branch: 'user-customization'
    - Description: Allow users to set the number of dice and the range of dice faces.
      
4. Save and Load Game State
    - Branch: 'save-load'
    - Description: Implement saving and loading of game states so users can resume from where they left off.
      
5. Improved User Interface
    - Branch: 'ui-enhancements'
    - Description: Enhance the user interface with better prompts, graphics, or a graphical user interface (GUI).
      
6. Multiplayer Mode
    - Branch: 'multiplayer'
    - Description: Add a multiplayer mode where multiple users can roll dice in a game setting.

## Contributing
Feel free to contibute by creating issues or submiting pull requests for any of the planned fetures or improvements.

## Usage
To use the Dice Simulation:
1. Run the script after completing the Installation steps from 1 - 5.
2. Load a file to save roll history (i.e., enter any filename of choice).
3. Playing:
   - 'Roll Dice' to roll.
   - 'Switch Dice' to switch dice from 1 to 2 & vice verse.
   - 'Save Game' to save current rolls.
   - 'Show Roll History' show history rolls.
   - 'Exit' to exit and can also choose to save the overall rolls from current rolls of the game or not. 

