# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}


def get_menu_items():
    """Retrieves the menu items 

    Returns:
        The menu_items list
    """
    menu_items = {}

    # Create a variable for the menu item number
    i = 1    

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    return menu_items


def get_customer_menu_category(menu_items):
    """Prints the list of menu categories and retrieves the customer's 
    selection

    Args:
        menu_items: The list of menu items

    Returns:
        The menu cateogory selected by the customer         
    """    
    menu_category = 0

    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")
    
    # Get the customer's input
    menu_category_str = input("Type menu number: ")

    if menu_category_str == "":
        menu_category = -1

    elif menu_category_str.isdigit() == False:
        menu_category = -1 

    else:
        menu_category = int(menu_category_str)

    # Check if the customer's input is a valid option
    if menu_category not in menu_items.keys():                           
         menu_category = 0

    return menu_category              



def get_customer_order(menu_items, menu_category, order_list):
    """Prints the menu items and gets the customer's menu item selection
     
    Args:
        menu_items: The menu items items list
        menu_category: The customer's selected menu category
        order_list: The customer's order list

    Returns:
        The customer's order list
    """
             
    # Save the menu category name to a variable
    menu_category_name = menu_items[int(menu_category)]
    # Print out the menu category name they selected
    print(f"You selected {menu_category_name}")

    # Print out the menu options from the menu_category_name
    print(f"What {menu_category_name} item would you like to order?")
    i = 1
    menu_items = {}
    print("Item # | Item name                | Price")
    print("-------|--------------------------|-------")
    for key, value in menu[menu_category_name].items():
        # Check if the menu item is a dictionary to handle differently
        if type(value) is dict:
            for key2, value2 in value.items():
                num_item_spaces = 24 - len(key + key2) - 3
                item_spaces = " " * num_item_spaces
                print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                menu_items[i] = {
                    "Item name": key + " - " + key2,
                    "Price": value2
                }
                i += 1
        else:
            num_item_spaces = 24 - len(key)
            item_spaces = " " * num_item_spaces
            print(f"{i}      | {key}{item_spaces} | ${value}")
            menu_items[i] = {
                "Item name": key,
                "Price": value
            }
            i += 1


    #Sub menu begin
    valid_response = False
    while True:                                        

        # 2. Ask customer to input menu item number
        menu_selection = input("Enter the menu item number: ")

        # 3. Check if the customer typed a number
        if menu_selection.isdigit() ==  False:
                #  Tell the customer they chose an invalid option
            print(f"Menu item number {menu_selection} is not a number.  Try again!")  

        else:                        
            menu_item_number = int(menu_selection)

            # Convert the menu selection to an integer                    
            if menu_item_number in menu_items.keys():
                valid_response = True

                # Store the item name as a variable
                item_name = menu_items[menu_item_number]["Item name"]
                item_price = menu_items[menu_item_number]["Price"]

                # Ask the customer for the quantity of the menu item
                quantity_str = input(f"Enter quantity of {item_name}: ")

                # Check if the quantity is a number, default to 1 if not
                if quantity_str.isdigit() == True:
                    quantity = int(quantity_str)
                else:
                    print(f"Quantity {quantity_str} is not a valid number. Entry will default to 1")
                    quantity = 1

                # Add the item name, price, and quantity to the order list
                order_list.append({
                    "Item name": item_name, 
                    "Price": item_price,
                    "Quantity": quantity
                })

            else:
                print(f"Menu item number {menu_selection} does not exist. Try again!")                                                                                    
                                                                                                        
            if valid_response:
                break   

    return order_list                                                        


def complete_order(order_list):
    """Totals the customer's order and prints the order receipt 
    for the customer

    Args:
        The customer's order list
    """
    # Print out the customer's order
    print("This is what we are preparing for you.\n")

    # Receipt header 
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")


    for item in order_list:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]          
       
        name_spaces = " " * (20 - len(item_name))
        price_spaces = " " * (6 - len(str(price)))
        print(f"{item_name}{name_spaces}      | {price}{price_spaces} | {quantity}")
        

    # 11. Calculate the cost of the order using list comprehension
    # Multiply the price by quantity for each item in the order list, then sum()
    # and print the prices.
    total_price = sum(x["Price"]*x["Quantity"] for x in order_list)
    print("\n" + f"The total for the order is ${total_price:,.2f}")



if __name__ == "__main__":

    # 1. Set up order list. Order list will store a list of dictionaries for
    # menu item name, item price, and quantity ordered
    order_list = []
    
    # Customers may want to order multiple items, so let's create a continuous
    # loop
    place_order = True
    while place_order:
         # Launch the store and present a greeting to the customer
        print("Welcome to the variety food truck.")

        # Create a dictionary to store the menu for later retrieval
        menu_items = get_menu_items()

        menu_category = get_customer_menu_category(menu_items)

        if menu_category == -1:
            print("Value entered is not a number!")

        elif menu_category == 0:
            print(f"Invalid menu category. Please try again!")

        else:
            order_list = get_customer_order(menu_items, menu_category, order_list)
            
            valid_response = False
            while True:

                # Ask the customer if they would like to order anything else
                keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

                # 5. Check the customer's input                 
                match keep_ordering.lower():
                    case 'y':
                        place_order = True
                        valid_response = True
                        break

                    case 'n':
                        print("Thank you for your order!")
                        place_order = False
                        valid_response = True
                        break 

                    case _:
                        print("Invalid input. Try again!")    

                if valid_response:  
                    break 
    
    if len(order_list) > 0:
        complete_order(order_list)
    else:
        print("Have a nice day!")