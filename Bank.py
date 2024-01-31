account1 = {
    "Name": "Ali",
    "accountNo": 1234,
    "Balance": 3000,
    "additionalBalance": 2000,
}

account2 = {
    "Name": "Ayşe",
    "accountNo": 4321,
    "Balance": 2000,
    "additionalBalance": 1000,
}

def money(account, amount):
        
    if account["Balance"] >= amount:
        newamount = account["Balance"] - amount
        account.update({
            "Balance": newamount
        })
        print("You can get your money.")
        print(f"Your remaining balance: {account["Balance"]}")
        print(f"Your remaining additional account balance: {account["additionalBalance"]}")
    else:
        toplam = account["Balance"] + account["additionalBalance"]
        
        if toplam >= amount:
            additionalBalance = input("Your balance is not sufficient. Do you want to use the additional account?(Y/N) ")
        
            if additionalBalance == "Y":
                x = amount - account["Balance"]
                newamount2 = account["additionalBalance"] - x
                account.update({
                    "Balance": 0,
                    "additionalBalance": newamount2
                })
                print("You can get your money.")
                print(f"Your remaining balance: {account["Balance"]}")
                print(f"Your remaining additional account balance: {account["additionalBalance"]}")
            elif additionalBalance == "N":
                print("The transaction was terminated and the exit was made.")
                quit()    
            else:
                print("Please write 'Y' or 'N'.")
                return additionalBalance           
        else:
            print("You do not have sufficient funds. The transaction has been terminated.")
            quit()
            
def main():
    print("Account Informations")
    print(account1)
    print(account2)
    print("")
    accountno = int(input("Account No: "))

    if accountno == 1234:
        print(f"Hi{account1["Name"]}.")
        money(account1, int(input("How much money would you like to withdraw? ")))
    elif accountno == 4321:
        print(f"Hi {account2["Name"]}.")
        money(account2, int(input("How much money would you like to withdraw? ")))
    else:
        print("account bulunamadı.")
        return accountno

main()    