import random
from collections import Counter
import json

results = []  # holds the results of each roll
roll_history = [] # list to store roll results

def roll_dice(): 
    """Function that rolls/simulates a random dice number between 1 and 6."""
    return random.randint(1, 6) 

def roll_single_die():
    """Function for rolling one die"""
    input("\nPress Enter to roll:\n")
    roll = roll_dice()
    print("You have rolled:", roll)
    results.append(roll) # stores results for a single die roll
    record_roll(roll) #Record the result

def roll_two_dice():
    """Function for rolling two dice"""
    input("\nPress Enter to roll:\n")
    roll1 = roll_dice()
    roll2 = roll_dice()
    print("You have rolled:", roll1,'and',roll2) 
    results.append((roll1, roll2))  # stores both dice rolls results
    record_roll((roll1,roll2))  # Record the result of both dice rolls

# Track Results

def display_results():
    """Function that display results of dice rolls"""
    print("\nHere Are Your Roll Results:")
    for i, result in enumerate(results,1):
        print(f"Roll {i}: {result}")
    print()

def record_roll(result):
    """Function that records the result of each dice roll into history for later analysis"""
    roll_history.append(result)

def get_roll_history():
    """Retrives the history of all recorded dice rolls"""
    return roll_history

def display_roll_history():
    """Function to display the history of dice rolls"""
    history = get_roll_history()
    print("\nRoll History:")
    for i, result in enumerate(history, 1):
        print(f"Roll {i}: {result}")

# Statistics Calculations

def calculate_statistics():
    """Function to calculate and display statistics of dice rolls."""
    # checks if there's anything in roll_history
    if not roll_history:
        print("No Rolls Recorded Yet!")
        return
    
    # flatten roll_history to make sure we can all dice rolls,
    # even if they were rolled as pairs
    """"Flattening" refers to the process of converting a complex structure, like a list of lists or a list of tuples, into a simpler, single-level list."""
    flattened_history = []
    for number in roll_history: # If number is a tuple (like from rolling two dice)
        if isinstance(number, tuple):
            flattened_history.extend(number) # Add each part of the tuple to the list
        elif isinstance(number, list): # # If number is a list (e.g., nested list)
            flattened_history.extend(number)
        else:
            flattened_history.append(number) # If it's a single number, just add it
    
    # using Counter to count how times each number appears in the list
    roll_counter = Counter(flattened_history)

    # display the stats
    print("\nRoll Statistics:")
    for num in range(1, 7):
        print(f"Number {num}: {roll_counter.get(num, 0)} times")
    
    print(f"\nTotal Rolls: {len(roll_history)}")

def load_game_state(filename):
    """Load a game state from a file"""
    global results, roll_history

    try:
        with open(filename, 'r') as file:  # opens reads the file
            game_state = json.load(file)
            results = game_state.get('results', [])
            roll_history = game_state.get('roll_history', [])
            print(f"Game state loaded from {filename}")
        
    except FileNotFoundError:
        print(f"No Saved Game State Found in {filename}\nStarting a new game.\n")
        results = []    # Start fresh if no saved state is found
        roll_history = []
    except json.JSONDecodeError:
        print(f"Failed to load game state from {filename}. The file might be corrupted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
def save_game_state(filename):
    """Save the current game state to a file"""
    game_state = { # dict to capture & organize the game's current data in one object
        'results': results,
        'roll_history': roll_history
    }
    try:
        with open(filename, 'w') as file: # opens the file according to the filename named by user, if not it does not exit it will be create
                                        # 'with' ensures that the file is properly closed after the block of code is executed.
            json.dump(game_state, file)  # 'game_state' is converted to a json format & writes it to the file.
            # 'json.dump' serializes(edits) game_state and makes it a readable & storable format.
        print(f"Game state saved to {filename}")
    except IOError as e:
        print(f"Failed to save game state to {filename}: {e}")
    except Exception as e:
        print("An unexpected error occured: {e}")

def main():

    print("\nWelcome to the Dice Simulation Game! \n")
    filename = input("Enter the filename to load your game state: ")
    load_game_state(filename) 

    while (True):
        while (True):  # makes sure user enter the correct input (type)
            try:
                choose = int(input("\nWould you like to roll 1 die or 2 dice?\n\nEnter (1 or 2): "))
                if((choose == 1) or (choose == 2)):
                    break
                else:
                    print("Wrong input! Please Enter 1 or 2")
            except ValueError:
                print("Invalid input! Please Enter a Number (1 or 2)")
        end_game = False  # Flag to indicate when to end the game
        while (True):
            if(choose == 1):
                roll_single_die()
            else:
                roll_two_dice()
                
            option = input(
                "\nWould you like to switch between 1 die and 2 dice? (enter switch)\n\n"
                "Continue playing? (enter play)\n\n"
                "See roll history? (enter h)\n\n"
                "Save game? (enter save)\n\n"
                "Or stop playing? (enter stop)\n\n"
                "I would like to: ").lower()

            if option == "play":
                continue # Repeats the loop, rolling the current choice of dice

            elif option == "switch":
                if (choose == 1):
                    choose = 2
                    print("You have changed to 2 dice!\n")
                elif (choose == 2):
                    choose = 1
                    print("You have change to 1 die!\n")

            elif option == "h":
                display_roll_history()  # Display the roll history

            elif option == "save":
                filename = input("Enter filename to save your game state: ")
                save_game_state(filename)
                
            elif option == "stop":
                end_game = True
                break # Exits the inner loop to end the game    
            else:
                print("Wrong Input! Please enter 'switch', 'play', 'h', or 'stop' ")
            
            if end_game:
                break   # Exits the outer loop to completely stop the game
                
        display_results() # Display the results of the dice rolls
        calculate_statistics() # Display the roll statistics
        print("\nThank You for Playing!")  # End of the game
        break  # Exit the outer loop to completely stop the game


if __name__=="__main__":
    main()

