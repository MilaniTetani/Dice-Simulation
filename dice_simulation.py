import random
from collections import Counter
import json
import os
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

class DiceSimulationApp:
    def __init__(self, root):
        """Initializes the game, loads dice images, and sets up the UI."""
        self.root = root
        self.root.title("Dice Simulation Game")

        self.results = []  # holds the results of each roll
        self.roll_history = [] # list to store roll results
        self.choose = 1 # Default to rolling 1 die
        self.dice_size = (100, 100)  # Define the desired size for dice images
        self.dice_images = self.load_resize_images()  # Load and resize dice images
        # Load dice images
        #self.dice_images = [ImageTk.PhotoImage(Image.open(f"die_face_{i}.png")) for i in range(1, 7)]
        self.setup_ui()  #Setup the Gui components
        self.load_game_state()  # Load game state on startup

    def load_resize_images(self):
        """Load dice images and resize them to the desired size."""
        images = []  # array of the images
        for i in range(1, 7):
            image = Image.open(f"die_face_{i}.png")
            resized_images = image.resize(self.dice_size, Image.LANCZOS)
            images.append(ImageTk.PhotoImage(resized_images))
        return images
    
    def setup_ui(self):
        """Sets up the user interface components for the dice simulation app."""
        
        # UI components
        # & Using grid for consistency

         # Dice image display
        self.dice_label = tk.Label(self.root)
        self.dice_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        # Result display
        self.result_label = tk.Label(self.root, text="Roll Result: ", font=("Arial", 16))
        self.result_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Roll button
        self.roll_button = tk.Button(self.root, text="Roll Dice", command=self.roll_dice, font=("Arial", 14))
        self.roll_button.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

        # Switch button
        self.switch_button = tk.Button(self.root, text="Switch Dice", command=self.switch_dice, font=("Arial", 14))
        self.switch_button.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

        # History button
        self.history_button = tk.Button(self.root, text="Show Roll History", command=self.display_results, font=("Arial", 14))
        self.history_button.grid(row=3, column=0, padx=5, pady=5, sticky='ew')

        # Save button
        self.save_button = tk.Button(self.root, text="Save Game", command=self.save_game_state, font=("Arial", 14))
        self.save_button.grid(row=3, column=1, padx=5, pady=5, sticky='ew')
                                                            #  sticky='ew': Makes the button stretch horizontally to fill the space in its cell.

        # Exit button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_game, font=("Arial", 14))
        self.exit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

        # Roll history display
        self.history_text = tk.Text(self.root, height=10, width=50, font=("Arial", 12))
        self.history_text.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')
                                                                            #   sticky='nsew': Makes the text box expand both horizontally and vertically within its cell.
         # Configure grid row and column weights
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def roll_dice(self): 
        """Function that rolls/simulates a random dice number between 1 and 6."""
        if self.choose == 1:
            roll = random.randint(1, 6) 
            self.result_label.config(text=f"Roll Results: {roll}")
            self.dice_label.config(image=self.dice_images[roll-1])  # Update dice image
            self.results.append(roll)  # stores results for a single die roll
            self.record_roll(roll) #Record the result
        else:
            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            self.result_label.config(text=f"Roll Result: {roll1} and {roll2}")

            # first dice image
            self.dice_label.config(image=self.dice_images[roll1-1])  # Update dice image for the first die

            # second Label to show the second dice image
            # Check if the object 'self' (which refers to the instance of the class) has an attribute called 'dice_label2'.
            # If 'self' does not have this attribute (i.e., 'dice_label2' doesn't exist yet), the code inside the if-block will run.
            if not hasattr(self, 'dice_label2'):
                # Create the 'dice_label2' attribute and assign it a new Label widget.
                self.dice_label2 = tk.Label(self.root)
                self.dice_label2.grid(row=0, column=1, pady=10)

            # Update the second dice image
            self.dice_label2.config(image=self.dice_images[roll2-1])
            
            self.results.append((roll1, roll2))  # stores both dice rolls results
            self.record_roll((roll1, roll2))  # Record the result of both dice rolls

    def switch_dice(self):
        self.choose = 2 if self.choose == 1 else 1
        messagebox.showinfo("Dice Simulation", f"Switched to {'2 dice' if self.choose == 2 else '1 die'}.")

    def display_results(self):
        """Function that display results of dice rolls"""
        self.history_text.delete(1.0, tk.END)
        for i, result in enumerate(self.roll_history, 1):
            self.history_text.insert(tk.END, f"Roll {i}: {result}\n")

    # Track Results
    def record_roll(self, result):
        """Function that records the result of each dice roll into history for later analysis"""
        self.roll_history.append(result)

    # Statistics Calculations
    def calculate_statistics(self):
        """Function to calculate and display statistics of dice rolls."""

        # checks if there's anything in roll_history
        if not self.roll_history:
            messagebox.showinfo("Dice Simualtion", "No Rolls Recorded Yet!")
            return
        
        # flatten roll_history to make sure we can all dice rolls,
        # even if they were rolled as pairs
        """"Flattening" refers to the process of converting a complex structure, like a list of lists or a list of tuples, into a simpler, single-level list."""
        flattened_history = []
        for number in self.roll_history: # If number is a tuple (like from rolling two dice)
            if isinstance(number, tuple):
                flattened_history.extend(number) # Add each part of the tuple to the list
            elif isinstance(number, list): # # If number is a list (e.g., nested list)
                flattened_history.extend(number)
            else:
                flattened_history.append(number) # If it's a single number, just add it
        
        # using Counter to count how times each number appears in the list
        roll_counter = Counter(flattened_history)

        # display the stats
        stats_message = "\nRoll Statistics:\n"
        for num in range(1, 7):
            stats_message += f"Number {num}: {roll_counter.get(num, 0)} times\n"
        
        stats_message = f"\nTotal Rolls: {len(self.roll_history)}"
        messagebox.showinfo("Dice Simulation", stats_message)

    def load_game_state(self):
        """Load a game state from a file"""
        filename =  filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        #global results, roll_history
        if filename:
            try:
                with open(filename, 'r') as file:  # opens reads the file
                    game_state = json.load(file)
                    self.results = game_state.get('results', [])
                    self.roll_history = game_state.get('roll_history', [])
                    messagebox.showinfo(f"Game state loaded from {filename}")
                
            except FileNotFoundError:
                messagebox.showinfo("Dice Simulation", f"No Saved Game State Found in {filename}\nStarting a new game...\n")
                self.results = []    # Start fresh if no saved state is found
                self.roll_history = []
            except json.JSONDecodeError:
                messagebox.showerror("Dice Simulation", f"Failed to load game state from {filename}. The file might be corrupted.")
            except Exception as e:
                messagebox.showerror("Dice Simulation", f"An unexpected error occurred: {e}")
            
    def save_game_state(self):
        """Save the current game state to a file"""
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            game_state = { # dict to capture & organize the game's current data in one object
                'results': self.results,
                'roll_history': self.roll_history
            }
        try:
            with open(filename, 'w') as file: # opens the file according to the filename named by user, if not it does not exit it will be create
                                            # 'with' ensures that the file is properly closed after the block of code is executed.
                json.dump(game_state, file)  # 'game_state' is converted to a json format & writes it to the file.
                # 'json.dump' serializes(edits) game_state and makes it a readable & storable format.
            messagebox.showinfo("Dice Simulation", "Game state saved successfully!")
        except IOError as e:
            messagebox.showerror("Dice Simulation", f"Failed to save game state: {e}")

    def exit_game(self):
        """Prompt to save the game state before exiting."""
        if messagebox.askyesno("Exit", "Would you like to save the game state before exiting?"):
            self.save_game_state()
        self.root.destroy()
    

if __name__=="__main__":
    root = tk.Tk()
    app = DiceSimulationApp(root)
    root.iconbitmap("./dice.ico")
    root.mainloop()

