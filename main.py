foodList = ["1 - Meatpie", "2 - Scroll", "3 - Juice", "4 - Checkout"]
Checkout = True

Name = input("Enter student name : ")

print(f"""Welcome {Name}!""")

def addingItems():
    while Checkout:
        for item in foodList:
            print(item)
        choice = input("Enter the number of the item you would like : ")
        if choice == 1:
            print("You chose the Meatpie")
        elif choice == 2:
            print("You chose the scroll")
        elif choice == 3:
            print("You chose the juice")
        elif choice == 4:
            print("Would you like to go to the checkout?")
#            checkoutChoice = input("Would you like to go to the Checkout? 1 for yes, 2 for no")
#            if checkoutChoice ==  1:
#                break   
      

addingItems()