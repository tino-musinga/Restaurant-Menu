"""The program below allow user to enter the food they want from the provided food list
prolist provided then prints out a receipt!"""

import sys #import statement used to import the module sys which contains a method that will be used to exit application on request

print("Mountain Wiew".center(60,"-")) #this prints out the Name of the restaurant and uses center align method to align the name of the restaurant at the center of 60 space
print("Concessions Menu".center(60, " "))
print("Pizza(cheese)".ljust(50,"."),"$3.25")
print("Pizza(pepperoni)".ljust(50,"."),"$3.25") # this prints Pizza(pepparoni) to the screen and left justifies it padding the remaining of 50 characters with a preiod
print("Pizza(sausage)".ljust(50,"."),"$3.25\n")
print("Hot dog".ljust(50,"."),"$2.25")
print("Nachos".ljust(50,"."),"$3.25")
print("Nachos(Extra Cheese)".ljust(50,"."),"$4.25\n")
print("Soft Pretzel".ljust(50,"."),"$2.75")
print("Churros".ljust(50,"."),"$2.00")
print("Cotton Candy".ljust(50,"."),"$2.25")
print("Popcorn".ljust(50,"."),"$2.50")
print("Chips".ljust(50,"."),"$1.50")
print("Candy (Butterfinger)".ljust(50,"."),"$1.50")
print("Candy (M&M's)".ljust(50,"."),"$1.50")
print("Candy (Peanut M&M's)".ljust(50,"."),"$1.50")
print("Candy (Skittles)".ljust(50,"."),"$1.50")
print("Candy (Snickers)".ljust(50,"."),"$1.50")
print("Candy (Starbust)".ljust(50,"."),"$1.50")
print("Candy (Twix)".ljust(50,"."),"$1.50\n")
print("Ice cream * Snow Cones".center(60," "))
print("Ice Cream".ljust(50,"."),"$2.75")
print("Snow Cone(Blue Berry)".ljust(50,"."),"$3.00")
print("Snow Cone(Cherry)".ljust(50,"."),"$3.00")
print("Snow Cone(Lime)".ljust(50,"."),"$3.00\n")
print("Beverages Regular $2.00 Large $2.50".center(60," "))
print("* Pepsi * Diet Pepsi * Cherry Pepsi".center(60," "))
print("* Mountain Dew * Orange Crush * Mug Root Beer".center(60," "))
print("* Sierra Mist * Tropicana Pink Lemonade\n".center(60," "))
print("Aquafina Water".ljust(50,"."),"$2.00")
print("Pure Leaf Tea".ljust(50,"."),"$2.50")
print("Gatorade".ljust(50,"."),"$2.50\n")

menu = {"pizza(cheese)":3.25, "pizza(pepperoni)":3.25, "pizza(sausage)":3.25, 
        "hot dog":2.25, "nachos":3.25, "nachos(extra cheese)":4.25,
       "soft pretzel":2.75, "churros":2.00, "cotton candy":2.25,
       "popcorn":2.50, "chips":1.50, "candy (butterfinger)":1.50,
      "candy (m&m's)":1.50, "candy (peanut m&m's)":1.50, "candy (skittles)":1.50,
      "candy (snickers)":1.50, "candy (starbust)":1.50, "candy (twix)":1.50,
     "ice cream":2.75, "snow cone(blue berry)":3.00, "snow cone(cherry)":3.00,
     "snow cone(lime)":3.00, "pepsi":2.00, "diet pepsi":2.00,
     "cherry pepsi":2.00, "mountain dew":2.00, "orange crush":2.00,
     "mug root beer":2.00, "sierra mist":2.00, "tropical pink lemonade":2.00,
     "aquafina water":2.00, "pure leaf tea":2.50, "gatorade":2.50}    #this is a dictionary that contains all the menu items that can be picked by the user, the key is the item and the value is the cost of the item

 
loop_control = True #this variable will be used to control the while loop
total_cost = [] #this list stores prizes of food items selected by user
selected_items = [] #this list stores food items items selected by the user

while loop_control: #this loop will continue running until the value of loop_control is changed to false
    food_item = input("ENTER YOUR FOOD ITEM and type 'done' when you're Done, 'cancel' to cancel order, 'restart' to restart your order : ") #this outputs a message on screen and collect user input that is the food item selected by the user
    if food_item.lower() == "done": #this condition checks if user is done entering food items and is ready to order food
        loop_control = False
        print("Thank you,your order is being processed!")
    elif food_item.lower() == "cancel": #this condition checks if user wants to cancel their order
        print("Thank you for using our service see you next time!")
        sys.exit() #this exits the application
    elif food_item.lower() == "restart": #this line check if customer wants to restart their order
        print("Your order is starting afresh!")
        total_cost = [] #after user restarts order the total cost list is initialized 
        selected_items = [] #after user restarts order the selected_items list is initialized
    else:
        try: #try statement used to catch an expected KeyError when the user enter food items that are not in the menu
            cost = menu[food_item.lower()] #the lower method converts user input to lowercase so that even if the user enters capital letters, the program will be able to search the value in dictionary menu
            if food_item.lower() == "pepsi" or  food_item.lower() == "diet pepsi" or food_item.lower() == "cherry pepsi" or food_item.lower() == "mountain dew" or food_item.lower() == "orange crush" or food_item.lower() == "mug root beer" or food_item.lower() == "sierra mist" or food_item.lower() == "tropicana pink lemonade": #if statement used to check if user selected a beverage
                beverage_size = input("Do you want 'regular' $2.00 or 'large' $2.50: ") #check if user wants regular or large beverage
                if beverage_size.lower() == "large":  
                    total_cost.append(2.50)
                    selected_items.append(food_item + " large") #append the beverage and size selected to the list of selected food items
                    for i in selected_items:  #prints the items selected to screen
                        print(i, end = " ")
                else:
                    total_cost.append(2.00)
                    selected_items.append(food_item)
                    for i in selected_items:
                        print(i, end = " ")
            else:
                print("items selected: ", end = "")
                selected_items.append(food_item)
                for i in selected_items:
                    print(i, end = " ")
                total_cost.append(cost)
        except KeyError:
            print("Make sure you enter the food item as it appears on the menu!") #catches KeyError exception if user enter food item that is not on the menu
        finally:
            print("")

if selected_items:
    print("RECEIPT".center(60,"*")) #this line print the string RECEIPT to screen and justifies it to the center of 60 character spaces 
    print("item".ljust(40," "), "cost")
    for i in range(len(selected_items)): #for statement runs number of times equal to the length of the list selected_items
        print(selected_items[i].ljust(40, "."), "${:.2f}".format(total_cost[i]))
    print("total cost before taxes".ljust(40,"."), "${:.2f}".format(sum(total_cost))) #prints total cost to the screen and left justifies it an pad the remain of 40 characters with a period, formats the price to 2 decimal places because its currency
    print("total cost after taxes".ljust(40,"."), "${:.2f}".format(sum(total_cost)*0.02 + sum(total_cost)))
    print("Thank you for stopping by!")

 