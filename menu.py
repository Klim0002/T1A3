import pandas as pd
import numpy as np

income = 0
expenses = []
budget = 0
streak = 0
difference = 0
entries = 0

def congrats():
    difference = int(budget) - int(amountToAdd)
                    
    if difference > 0:
            print(difference)
            print("yay!") 
            streak = streak + 1
        
    else:
        streak = 0
        print("oh no! you're over budget")

def option_1():
    print("what is your income?")
    income = input(" > ")
    print("what is your budget?")
    budget = input(" > ")
    budget_percentage = (int(budget) / int(income) * 100)
    str(budget_percentage)
    print("\n\n")
    print("your income is " + str(income) + " and your budget is " + str(budget) + ". This makes your budget " + str(budget_percentage) + "%" + " of your income.")
    print("\n\n")
    file = open("record.txt", "a")
    file.write("\n income=" + income)
    file.write("\n budget=" + budget)
    
def option_2(date, amount):
    expense = {"date": date, "amount": amount }
    expenses.append(expense)
        
    
        

def option_3():
    print("\nHere is a list of your expenses...")
    print("------------------------------------")
    counter = 0
    for expense in expenses:
        print("#" , counter, " - ", expense["date"], " - ", expense["amount"])
        counter += 1
    print("\n\n")
    file = open("record.txt", "a")
    file.write(expense)
    


def option_4():
    average = (option_2(difference_sum) / option_2[counter])
    print(average)

def option_5():
    print(option_2(streak))
    
def option_6():
    file = open("record.txt", "a")
    file.write("\n" + expenses)
    



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
                    try:
                        option_1()
                        break
                    except:
                        print("invalid")
                        break    
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
                    amountToAdd = input("> ")
                    break       
                except:
                    print("Invalid input. Please try again.")
            
            congrats()
            option_2(date, amountToAdd)
                    
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

