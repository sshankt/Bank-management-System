import cv2  # Note: This import is not used in the code
import pyttsx3
engine = pyttsx3.init() 
balance = 0
pin = 76321

def deposit_money(amount):
    global balance 
    balance += amount
    print(f"You deposited {amount} rupees.")
    engine.say(f"You deposited {amount} rupees.")
    engine.runAndWait() 
def withdraw_money(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"You withdrew {amount} rupees.") 
        print(f"Your current Amount :{balance}") 
        engine.say(f"You withdrew {amount} rupees.") 
        engine.say(f"Your current Amount :{balance}")
        engine.runAndWait() 
    else: 
        print(f"you do not have enough money\nyour current balance is :{balance}")
        engine.say(f"You do not have enough money\n Your current balance is: {balance}")
        engine.runAndWait()
def check_balance():
    print(f"Your current balance is: {balance}") 
    engine.say(f"Your current balance is: {balance}") 
    engine.runAndWait() 
print("--------------------------------------------------------")
print("=============== Bank Management System ===============")
print("----------------------------------------------------------------")
engine.say("Welcome to The Bank Management System  ")
engine.runAndWait()
while True:
    print("Press\n 1. Deposit\n 2. Withdraw\n 3. Check balance\n 4. Exit")
    print("-------------------------------------------------")
    user = input("Enter how you would like to proceed: ")
    print("--------------------------------------------------")

    match user:
        case "1":
            engine.say("You choice for Deposit money")
            engine.say("Plese Enter The Amount ")
            engine.runAndWait() 
            amount = int(input("Enter the amount: "))
            pincode = int(input("Enter your PIN: "))
            if pincode == pin:
                deposit_money(amount) 
            else:
                print("Wrong PIN.")

        case "2":
            engine.say("You choice for Withdraw money")
            engine.say("Plese Enter The Amount ")
            engine.runAndWait() 
            amount = int(input("Enter the amount: "))
            pincode = int(input("Enter your PIN: "))
            if pincode == pin:
                withdraw_money(amount) 
            else:
                print("Wrong PIN.")

        case "3":
            engine.say("You choice for Check blance")
            
            engine.runAndWait() 
            pincode = int(input("Enter your PIN: "))
            if pincode == pin:
                check_balance()
            else:
                print("Wrong PIN.")

        case "4":
            print("Thank you for visiting!")
            engine.say("Thank you for visiting!")
            engine.runAndWait() 
            break  # Exit the loop

        case _:
            print("Invalid option. Please try again.")
