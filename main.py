foodList = ["1 - Meatpie, $5", "2 - Scroll, $10", "3 - Juice, $3", "4 - Checkout"]
Checkout = True

item_name = ""
price = 0

Name = input("Enter student name : ")

print(f"""Welcome {Name}!""")

def receipt(item_name, price):
    print("\n----- RECEIPT -----")
    print("Item:", item_name)
    print("Price: $", price)
    print("-------------------")

def addingItems():
    while Checkout:
        for item in foodList:
            print(item)
        choice = int(input("Enter the number of the item you would like: "))

        if choice == 1:
            item_name = "Meatpie"
            price = 5
            print("You chose the Meatpie")
            receipt("Meatpie", 5)
            break
        elif choice == 2:
            item_name = "Scroll"
            price = 10
            print("You chose the scroll")
            receipt("Scroll", 10)
            break
        elif choice == 3:
            item_name = "Juice"
            price = 3
            print("You chose the juice")
            receipt("Juice", 3)
            break
        else:
            print("Invalid choice")
            return

addingItems()