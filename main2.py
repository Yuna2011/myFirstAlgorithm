foodList = ["1 - Meatpie, $5", "2 - Scroll, $10", "3 - Juice, $3", "4 - Dubai Chocolate Strawberry Matcha, $100"]
yourList = []
Checkout = True

item_name = ""
price = 0

Name = input("Enter student name : ")

print(f"""Welcome {Name}! Here is the menu: """)
print("If you spend over $10, you get a 10% discount!!")

def receipt(item_name, price):
    print("\n----- RECEIPT -----")
    print(Name)
    print("Items:", item_name)
    print("Price: $", price)
    print("-------------------")

def moreItems():
    More = int(input("Would you like to add more to your list? Enter 1 for yes and 2 to head to the checkout: "))
    if More == 1:
        for item in foodList:
            print(item)
    elif More == 2:
        if price > 10:
            price = price*0.9
    else:
        print("Invalid choice")
        for item in foodList:
            print(item)
        return

def addingItems():
    while Checkout:
        for item in foodList:
            print(item)
        choice = int(input("Enter the number of the item you would like: "))

        if choice == 1:
            item_name = "Meatpie"
            price = 5
            print("You chose the Meatpie")
            yourList.append(item_name)
            moreItems()
        elif choice == 2:
            item_name = "Scroll"
            price = 10
            print("You chose the scroll")
            yourList.append(item_name)
            moreItems()
        elif choice == 3:
            item_name = "Juice"
            price = 3
            print("You chose the juice")
            yourList.append(item_name)
            moreItems()
        elif choice == 4:
            item_name = "Dubai Chocolate Strawberry Matcha"
            price = 100
            print("You chose the Dubai Chocolate Strawberry Matcha")
            yourList.append(item_name)
            moreItems()
        else:
            print("Invalid choice")
            print(*foodList)
            return
        
        if price > 10:
            price = price*0.9
        receipt(item_name, price)
        break

addingItems()