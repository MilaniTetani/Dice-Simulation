import random

results = []  # holds the results of each roll

def roll_dice(): 
    """Function that rolls/simulates a random dice number between 1 and 6."""
    return random.randint(1, 6) 

def roll_single_die():
    """Function for rolling one die"""
    input("\nPress Enter to roll:\n")
    roll = roll_dice()
    print("You have rolled:", roll)
    results.append(roll) # stores results for a single die roll

def roll_two_dice():
    """Function for rolling two dice"""
    input("\nPress Enter to roll:\n")
    roll1 = roll_dice()
    roll2 = roll_dice()
    print("You have rolled:", roll1,'and',roll2) 
    results.append((roll1, roll2))  # stores both dice rolls results

def display_results():
    """Function that display results of dice rolls"""
    print("\nHere Are Your Roll Results:")
    for i, result in enumerate(results,1):
        print(f"Roll {i}: {result}")
    print()

def main():
    print("\nWelcome to the Dice Simulation Game! \n")

    while (True):
        choose = int(input("Would you like to roll 1 die or 2 dice? \n Enter (1 or 2): "))

        while (True):
            if(choose == 1):
                roll_single_die()
            elif(choose == 2):
                roll_two_dice()
            else:
                print("Wrong input! Please Enter 1 or 2")
            
            option = input("\nWould you like to switch between 1 die and 2 dice? (enter switch)\nContinue playing? (enter play)\nOr stop playing? (enter stop)\nI would like to: ")

            if option.lower() == "play":
                continue # Repeats the loop, rolling the current choice of dice

            elif option.lower() == "switch":
                if (choose == 1):
                    choose = 2
                    print("You have changed to 2 dice!\n")
                    #roll_two_dice()
                elif (choose == 2):
                    choose = 1
                    print("You have change to 1 die!\n")
                    #roll_single_die()
            
            elif option.lower() == "stop":
                break # Exits the inner loop to end the game
            
            else:
                print("Wrong Input! Please enter 'switch', 'play', or 'stop' ")
                #continue
            
        display_results()
        print("\nThank You for Playing!")  # End of the game
        break  # Exit the outer loop to completely stop the game


if __name__=="__main__":
    main()

