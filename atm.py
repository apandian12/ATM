from cardHolder import cardholder

def print_menu():
    ### print optioms to the user
    print("please choose from one of the following options...")
    print("1. deposit")
    print("2. withdraw") 
    print("3. show balance")
    print("4. exit")

def deposit(cardholder):
    try:
        deposit = float(input("how much would you like to deposit: "))
        cardholder.set_balance(cardholder.get_balance()+ deposit)
        print("your new balance is: ", str(cardholder.get_balance()))
    except:
        print("invaild input")

def withdraw(cardholder):
    try:
        withdraw = float(input("how much would you like to withdraw: "))
        ## check if user has enough money
        if(cardholder.get_balance() < withdraw):
            print("insufficient balance :(")
        else:
            cardholder.set_balance(cardholder.get_balance() - withdraw)
            print("you're good to go! thankyou :)")   
    except:
        print("invaild input")

def check_balance(cardholder):
    print("your current balance is: ", cardholder.get_balance())

if __name__ =="__main__":
    current_user = cardholder("","","","","")

    ## create a repo of cardholders
    list_of_cardholders =[]
    list_of_cardholders.append(cardholder("1234567890", 1234,"bala", "kumar", 2500))
    list_of_cardholders.append(cardholder("0987654321", 5678, "raj", "kumar", 3000))
    list_of_cardholders.append(cardholder("2345678901", 9012, "ajith", "kumar",4000 ))
    list_of_cardholders.append(cardholder("3456789012", 3456, "dhinesh", "kumar", 5000))
    list_of_cardholders.append(cardholder("4567890123", 7890, "arun", "kumar", 8000))
    list_of_cardholders.append(cardholder("4567890124", 7890, "kiruba", "nidhi", 50000))
    

    ## promt user for debit card number
    debitcardNum = ""
    while True:
        try:
            debitcardNum = input("please insert your debit card: ")
            ## check against repo
            debitmatch =[holder for holder in list_of_cardholders if holder.cardNum == debitcardNum]
            if (len(debitmatch) > 0):
                 current_user = debitmatch[0]
                 break
            else:
                print("card number not recognized. please try again.")
        except:
            print("card number not recognized. try again.")

    ## promt for pin
    while True :
        try:
            user_pin = int(input("please enter your pin: ").strip())
            if(current_user.get_pin() == user_pin):
                break
            else:
                print("invaild pin. please try again.")
        except:
            print("invaild pin.please try again.")

    ## print options
    print("welcome", current_user.get_firstname()," :)")
    option = 0
    while (option !=4):
        print_menu()
        try:
            option = int(input())
        except:
            print("invaild input . please try again.")

        if(option == 1):
            deposit(current_user)
        elif(option == 2):
            withdraw(current_user)
        elif(option == 3):
            check_balance(current_user)
        elif(option == 4):
            break
        else:
            option = 0

    print("Thank you. have a nice day :)")