import random

def roll_dice(): # function that rolls/simulates a random dice number 1 - 6
    return random.randint(1, 6) 

def main():
    print("\nWelcome to the Dice Simulation Game! \n")
    while (True):
        input("Press Enter to play:\n")
        number = roll_dice()
        print("You have rolled:", number)
        reply = input("\nDo you want to play again? \nEnter (yes/no): ")
        if (reply == "no"):
            break
        
    print("\nThank You for Playing!")

if __name__=="__main__":
    main()

