from time import sleep
from random import randint
import json

def validateInput(listOfExpectedAnswers:list, hint:str):
    answer = input(hint)
    while answer not in listOfExpectedAnswers:
        answer = input("You've entered invalid answer")
    return answer


userAccounts = []
def registeration(email, password, phoneNum, fullName):

    try:
        # Load existing data from the database.json file
        with open('database.json', 'r') as file:
            data = file.read()
            if data:
                userAccounts = json.loads(data)
            else:
                userAccounts = []
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    
    for account in userAccounts:
        if account['email'] == email:
            return "Email exists, try another email."

    # Create a new account dictionary
    new_account = {"email": email, "password": password, "phone": phoneNum, "fullName": fullName, "Balance": randint(100, 1000)}

    # Append the new account to the list
    userAccounts.append(new_account)

    # Save the updated data back to the database.json file
    with open('database.json', 'w') as file:
        json.dump(userAccounts, file)




    account = login(email=email, password=password)

    input2 = validateInput(hint="How can we help you today? \n1. View Account Details\n2. Deposit\n3. Withdraw\n4. Cancel\n", listOfExpectedAnswers=['1','2','3', '4'])
    print_processing()

    if input2 == "1":
        print("BALANCE:", account['Balance'])
        print("EMAIL:", account['email'])
        print("Full Name:", account['fullName'])
        print("PHONE NUM:", account['phone'])

    elif input2 == "2":
        account['Balance'] += int(input('Enter amount to deposit '))
        print(f"Your balance now is {account['Balance']}")

    elif input2 == "3":
        account['Balance'] -= int(input('Enter amount to withdraw '))
        print(f"Your balance now is {account['Balance']}")
    elif input2 == "4":
        exit()


    return "Regsitered Successfully..."


def print_processing():
    print("Processing...")
    sleep(2)


def login(email, password):
    for account in userAccounts:
        if account['email'] == email and account['password'] == password:
            print('Login Successfuly.')
            return account
    return "Email or password did not match any accounts in our database :'("
