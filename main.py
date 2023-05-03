# app starts here
def start_menu():
    int(input("Which option would you like to take? \n 1. define budget \n 2. start data input \n 3. Reset \n 4. print data "))
try:  
    if 1:
        expense_budget()
    elif 2:
        income_expense()
    elif 3:
        delete_info()
    elif 4:
        record = open("record.txt", "r")
        print(record.read())
        record.close()
        input("return to the beginning? y/n")
        if "y":
            start_menu
        else:
            exit
except ValueError:
    print("invalid input")
    
    
        
def expense_budget():
    int(input("what is your daily budget?"))
    add to record.txt
    run income_expense
    
def delete_info():
    with open("record.txt",'w') as file:
        pass
    print("done")
    input("return to the beginning? y/n"):
    if "y":
        start_menu
    else:
        exit
    
def income_expense():
       {
        "date": inpute(date)
        "income": input(income?)
        "expense": input (expense)
        "yay or nay": pass or fail
        }
    date = input( "what is todays date?")
    income = int(input("was there any income"))
    expense = int(input("what is todays expenses?"))
    pass =  expense <= expense budget
    fail = expense => expense budget
    
    if 
        pass
        print("nice work! keep it up!")
        
    else:
        print("uh oh.... try again tomorrow")
        fail
    then if previous entry were yay print streak = i + 1 
    else: 
        print("streak not found")
    record = open("record.txt". "a")
    record.write("\nadded data")
    
    