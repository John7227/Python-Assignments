balance = 1000
while(True):
    atm = """
ATM 

1. Deposit
2. Withdraw
3. Check Balance
4. Exit
"""
    print(atm)
    atm_choice = int(input("Enter ATM Choice: "))

    match atm_choice:
        case 1: 
            deposit = int(input("Deposit: "))
            balance = deposit + balance
            print("Balance is", balance)
        case 2: 
            withdraw = int(input("Withdraw: "))
            if balance >= withdraw:
                balance = balance - withdraw
                print("Balance is", balance)
            else:
                print("Insufficient Funds")
        case 3: 
            print("Check Balance", balance)
        case 4: 
            print("Get Out Joor!")
            break
