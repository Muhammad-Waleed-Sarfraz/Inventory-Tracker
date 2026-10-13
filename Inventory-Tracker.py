import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

inventory = {}
while True:
    clear_screen()
    print("1. Add Inventory\n2. Remove Inventory\n3. View Inventory\n4. Update Stock\n5. Search Specific Item\n6. Exit")
    choice = input("Choose an Option : ")
    if choice in ["1","2","3","4","5","6"]:
        if (choice == "1"):
            clear_screen()
            item_name = input("Write item name : ")
            price = float(input("Write price for the item : "))
            quantity = int(input("Write quantity of the items : "))
            item_id = input("Write item ID ( e.g. 001) : ")
            inventory[item_id] = {
                "item_name" : item_name,
                "price" : price,
                "quantity" : quantity,
                "item_id" : item_id
                }
            print(f"successfull {item_name} added to the inventory")
            input("\nPress Enter to continue.....")
        elif (choice == "2"):
            clear_screen()
            remove_item = input("Write item ID you want to remove : ")
            if remove_item in inventory:
                delete_item = inventory[remove_item]['item_name']
                del inventory[remove_item]
                print(f"successfull ! {delete_item} has been removed")
            else:
                print(f"{remove_item} no found in the inventory")
            input("\nPress enter to continue.....")
        elif (choice == "3"):
            clear_screen()
            print("-"*75)
            print(f"| {'ID':<15} | {'Name':<15} | {'Qty':<15} | {'Price':<15} | {'Total Price':<15}|")
            for item_id, info in inventory.items():
                total_value = info['quantity']*info['price']
                print(f"| {item_id :<15} | {info['item_name']:<15} | {info['quantity']:<15} | ${info['price']:<15.2f} | ${total_value:<15.2f} ")

            print("-"*75)
            input("\nPress enter to continue.....")
        elif (choice == "4"):
            clear_screen()
            update_id = input("Enter Item ID to update : ")
            if update_id in inventory:
                print(f"----Editing Stock {inventory[update_id]['item_name']}----")
                print("\n1. Change item\n2. Change Quantity\n3. Change Price\n4. Change ID\n5. Exit")
                sub_choice = input("Choose an option : ")
                if sub_choice in ["1","2","3","4","5"]:
                    if (sub_choice == "1"):
                        clear_screen()
                        new_item = input(" Write new item name : ")
                        inventory[update_id]['item_name'] = new_item
                        print(f"{new_item} has been added")
                        input("\nPress enter to continue.....")
                    elif(sub_choice == "2"):
                        clear_screen()
                        update_qty = inventory[update_id]['quantity']
                        print(f"Current quantity for {inventory[update_id]['item_name']} : {update_qty}")
                        stock_change = int(input("Enter amount to add (Use negative sign to reduce value) : "))
                        inventory[update_id]['quantity'] += stock_change
                        print(f"Successfull! New quantity is now {inventory[update_id]['quantity']}")
                        input("\nPress enter to continue.....")
                    elif(sub_choice == "3"):
                        clear_screen()
                        new_price = float(input("Enter New Price : "))
                        inventory[update_id]['price'] = new_price
                        print(f"Successfull! New Price is {new_price}")
                        input("\nPress enter to continue")
                    elif (sub_choice == "4"):
                        clear_screen()
                        new_id = input(" Write New Id for the item : ")
                        inventory[new_id] = inventory.pop(update_id)
                        inventory[new_id]['item_id'] = new_id
                        print(f" Successfull! New item ID is {new_id}")
                        input("\nPress Enter to continue")
                    elif (sub_choice == "5"):
                        print("-----Exit! Return to main menu----")
                        input("\nPress enter to conyinue....")
                else:
                    print("-----Invalid Choice-----")
                    input("\nPress enter to continue.....")
            else:
                print(f"-----ID not Found-----")
                input("\nPress enter to continue....")
        elif (choice == "5"):
            clear_screen()
            search_id = input (" Write item ID to search : ")
            if search_id in inventory:
                info = inventory[search_id]
                item_total = info['quantity'] * info['price']
                print(f"\n----Item Details For ID : {search_id}----")
                print(f"Name       : {info['item_name']}")
                print(f"Price       : ${info['price']}")
                print(f"Stock Avalaible     : {info['quantity']}")
                print("-"*32)
                print(f"Toatal Value      : ${item_total:.2f}")
                print("-" *32)
                input("\nPress enter to continue.....")
            else:
                print(f"ID {search_id} not found in inventory")
                input("\nPress enter to continue....")
        elif(choice == "6"):
            clear_screen()
            print("-_-"*54)
            print("-----Thank You For Using-----".center(150))
            print("----- Good Bye -----".center(150))
            print("-_-"*54)
            break
    else:
        clear_screen()
        print("------Inalid Choice------")
        input("\nPress enter to continue.....")



    