import pandas as pd
import numpy as np

BUDGET = []
DATE = []
DIFFERENCE = []
AMOUNT = []
streak = 0
entries = 0



def option_1():
    
    BUDGET.append(budget)
    budget_percentage = (int(budget) / int(income) * 100)
    str(budget_percentage)
    print("\n\n")
    print("your income is " + income + " and your budget is " + budget + ". This makes your budget " + str(budget_percentage) + "%" + " of your income.")
    print("\n\n")

def option_2(date, amount, budget, differences):
    streak = 0
    entries = 0
    DATE.append(date)
    AMOUNT.append(amount)
    BUDGET.append(budget)
    DIFFERENCE.append(differences)
    difference = int(budget) - int(amount)
        
    
    if (difference > 0):
        print("\n\n")
        print(difference)
        print("yay!")
        print("\n\n") 
        streak = streak + 1
        entries = entries + 1
        difference = differences
        
    else:
        streak = 0
        entries = entries + 1
        difference = differences
        print("\n\n")
        print("oh no! you're over budget")
        print("\n\n")
      
    
        
# create a data frame to add expenses and to print
def option_3():
    expense_report = pd.DataFrame()
    expense_report["DATE"] = DATE
    expense_report["AMOUNT"] = AMOUNT
    expense_report["BUDGET"] = BUDGET
    expense_report["DIFFERENCE"] = DIFFERENCE
    expense_report.to_csv("expenses.csv")
    print(expense_report)

    


def option_4():
    average = option_2[difference] / option_2(entries)
    print(average)

def option_5():
    print(option_2(streak))
    

    



# menu
def menu():
    print("welcome to income and expense streak. choose from the following.")
    print("if this is your first time press 1.")
    print("option 1. insert income and budget")
    print("option 2. add total expense for the day")
    print("option 3. see all past expenses")
    print("option 4. what is the average overage?")
    print("option 5. what is your current streak?")
    print("option 0. exit")



if __name__ == "__main__":
    while True:
        menu()
        options = input(" > ")
        if (options == "1"):
                while True:
                    print("what is your current income?")    
                    try:
                        income = input(">")
                        break
                    except:
                        print("invalid")
                        
                while True:
                    print("what is your current budget?")    
                    try:
                        budget = input(">")
                        break
                    except:
                        print("invalid")
                option_1()        
                
                
                         
        elif (options == "2"):
            while True:
                print("what is the date?")
                try:
                    date = input("dd/mm/yy > ")
                    break
                except:
                    print("Invalid input. Please try again.")
                    
            print("what is the total amount of expenses for the day?")    
            while True:
                try:
                    amount = input("> ")
                    break       
                except:
                    print("Invalid input. Please try again.")
            
            difference = int(budget) - int(amount)
            option_2(date, amount, budget, difference)
                    
        elif (options == "3"):
            option_3()
            
        elif (options == "4"):
            option_4()
            
        elif (options == "5"):
            option_5()
        elif (options == "0"):
            quit()
        else:
            print("invalid function")
            


# create a data frame to add expenses


