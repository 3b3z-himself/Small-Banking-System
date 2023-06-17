from utils import validateInput, registeration, print_processing, login
from random import choice

def main():
    choosenBank = choice(['AAM BANK', 'MAA BANK', 'AMA BANK'])

    print(f"Welcome to {choosenBank} !, how can we help you today :) ?")
    print_processing()

    input1 = validateInput(hint="How can we help you today? \n1. Login\n2. Register\n3. Cancel\n", listOfExpectedAnswers=['1','2','3'])
    print_processing()

    if input1 == "1":
        email = input('ENTER UR EMAIL')
        password = input("ENTER UR PASSWORD")

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
    elif input1 == "2":
        email = input('ENTER UR EMAIL: ')
        password = input("ENTER UR PASSWORD: ")
        fullName = input("ENTER UR FULLNAME: ")
        phone = input("ENTER UR PHONENUM: ")
        registeration(email=email, password=password, fullName=fullName,phoneNum=phone)
    elif input1 == "3":
        exit()

    
main()




