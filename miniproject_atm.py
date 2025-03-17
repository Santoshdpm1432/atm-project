#
# balance = 0
# services = '''
# ========atm services======
# 1. credit
# 2. debit
# 3. blance
# 4. exit
# '''
# print(f"here is the services of our ATM {services}")
# def get_choice():
#     return input("enter your which service you want in choice (1-4)")

# def credit():
#     global balance
#     print("you choose to credit amount")
#     amount = float(input("enter how much you want to  credit :"))
#     if amount <= 0:
#         print("please enter valid amount to credit,thank you ")
#     else :
#         amount += balance
#         print(f"{amount}credited successfully")

balance = 0  # Global balance variable

services = '''
======== ATM Services ========
1. Credit
2. Debit
3. Balance
4. Exit
'''

print(f"Here are the available services of our ATM:\n{services}")

def get_choice():
    return input("Enter the number of the service you want (1-4): ")

def credit():
    global balance
    print("You chose to credit an amount.")
    amount = float(input("Enter how much you want to credit: "))
    
    if amount <= 0:
        print("Please enter a valid amount to credit. Thank you.")
    else:
        balance += amount  # Update global balance
        print(f"{amount} credited successfully. New balance: {balance}")

def debit():
    global balance
    print("You chose to debit an amount.")
    amount = float(input("Enter how much you want to debit: "))
    
    if amount <= 0:
        print("Please enter a valid amount to debit. Thank you.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount  # Deduct from balance
        print(f"{amount} debited successfully. Remaining balance: {balance}")

def show_balance():
    print(f"Your current balance is: {balance}")

# Main loop
while True:
    choice = get_choice()
    
    if choice == "1":
        credit()
    elif choice == "2":
        debit()
    elif choice == "3":
        show_balance()
    elif choice == "4":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")


    
