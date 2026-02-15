foodList = ["1 - Meatpie, $5", "2 - Scroll, $10", "3 - Juice, $3", "4 - Dubai Chocolate Strawberry Matcha, $100"]
yourList = {}
total = 0
Checkout = False

item_name = ""
price = 0

Name = input("Enter student name : ")

print(f"""Welcome {Name}! Here is the menu: """)
print("If you spend over $10, you get a 10% discount!!")

def receipt(item_name, price):
    print("\n----- RECEIPT -----")
    print(Name)
    print("Items:", ", ".join((f"{qty} {item}" for item, qty in yourList.items())))
    print("Price: $", price)
    if total > 10:
        print("The 10% discount has been applied")
    print("-------------------")

def again():
    global Checkout
    More = int(input("Would you like to add more to your list? Enter 1 for yes and 2 to head to the checkout: "))
    if More == 1:
        Checkout = False
    elif More == 2:
        Checkout = True
    else:
        again()

def extraStuff(item_name, price): 
    global total 
    print("You chose the", item_name) 
    if item_name in yourList: 
        yourList[item_name] += 1 
    else: 
        yourList[item_name] = 1
    total += price
    again()

def discount(total):
    if Checkout == True:
        if total > 10:
            total = total*0.9
    receipt(item_name, total)


def addingItems():
    global total
    while Checkout == False:
        for item in foodList:
            print(item)
        choice = int(input("Enter the number of the item you would like: "))

        if choice == 1:
            item_name = "Meatpie"
            price = 5
            extraStuff(item_name, price)
        elif choice == 2:
            item_name = "Scroll"
            price = 10
            extraStuff(item_name, price)
        elif choice == 3:
            item_name = "Juice"
            price = 3
            extraStuff(item_name, price)
        elif choice == 4:
            item_name = "Dubai Chocolate Strawberry Matcha"
            price = 100
            extraStuff(item_name, price)
        else:
            print("Invalid choice")
            again()
            return

    discount(total)
    
addingItems()