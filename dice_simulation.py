import random

def roll_dice(): 
    """Function that rolls/simulates a random dice number between 1 and 6."""
    return random.randint(1, 6) 

def roll_single_die():
    """Function for rolling one die"""
    input("Press Enter to roll a die:\n")
    roll = roll_dice()
    print("You have rolled:", roll)

def roll_two_dice():
    """Function for rolling two dice"""
    input("Press Enter to roll the dice:\n")
    roll1 = roll_dice()
    roll2 = roll_dice()
    print("You have rolled:", roll1,'and',roll2)    

def main():
    print("\nWelcome to the Dice Simulation Game! \n")

    choose = int(input("Would you like to 1 die or 2 dice? \n Enter (1 or 2): "))

    if(choose == 1):
        while (True):
            roll_single_die()
            reply = input("\nDo you want to play again? \nEnter (yes/no): ")
            if (reply.lower() == "no"):
                break

    elif(choose == 2):
        while (True):
            roll_two_dice()
            reply = input("\nDo you want to play again? \nEnter (yes/no): ")
            if (reply.lower() == "no"):
                break 
    else:
        print("Wrong input! Please Enter 1 or 2")
    
        
    print("\nThank You for Playing!")  # End of the game

if __name__=="__main__":
    main()

