try:
    import sys as s #importing library sys for programme control feaures
except ImportError:
    print("This programme could not be run as the libraries could not be retrived.")
employees = ["Mike", "James", "Ivy", "Joshua", "Barbra", "Jenny", "Aidan", "Macy", "John", "Lucy"]#employee names
toppings = ["blank", "1) Margarita", "2) Marinara","3) Pepperoni", "4) Veggie", "5) Chicken", "6) Four cheeses", "7) Hawaiian"] #toppings
prices = ["blank", 7.99, 8.99, 9.99, 9.99, 7.99, 9.99, 8.99] #prices for each topping
sales = []

def intro():
        global isEmployee  
        print("Welcome to the pizza sales management.")
        isEmployee = input("Enter a employees name to log their sales:")
        if isEmployee not in employees:
            print("Please enter an employees name.")
            intro()
        return;
intro()

def menu():
    for x in range(1, 8):
        print(toppings[x]) #prints list of toppings
    print("Now choose the amount sold per topping")
    menupick = 0 #sets the default value for the menu pick before the user has interacted
    while menupick != "8": #run the code below if the user doesnt put in 8
        try:
            menupick = int(input("Input a number from the list: "))
            amount = int(input("How many were sold? (Put 0 if none were sold.): "))
            total = prices[menupick] * amount #work out how much money is made
            pizza = toppings[menupick] 
            results = [isEmployee, pizza , total] #defines the values wanted in the text files
            sales.append(total)
            print("Here are the results:")
            print(isEmployee, "made £", total, "from this topping. This has been logged.")#outputs how much money an employee made in sales
        except ValueError:
            print("Please enter integers only.")
            menu()
        except IndexError:
            print("Please enter a number between 1 and 7 only.")
            menu()

        try:
            file = open("Sales.txt", "a")#opens the file and commands we add to it
            file.write("\n".join(map(lambda x: str(x), results)) + "\n") #converts the contents of the list into strings
            file.close()#closes the file
        except IOError:
            print("ERROR: File 'Sales.txt' could not be found.")
            s.exit("Error")
        repeat = input("Do you want to add more values?").lower()
        if repeat == "yes":
            print("Okay...")
            menu()
        else:
            print("Okay, here is the summary:")
            amount_made = sum(sales)
            print(isEmployee, "made a total of: £" + str(amount_made))
            print("With a total of ", amount, " pizzas sold")
            s.exit("Programme ended")
        return;
menu()

    



    
    
   
