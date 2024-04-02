# Welcome to Variety Food Truck

This is an interactive ordering system for a food truck menu.  With this system a customer can place an order and receive a receipt with the total price of all items ordered.  The menu will display multiple categories for a customer to choose from and can choose food items until done ordering.  See screen shots below:

![Screenshot 2024-04-02 115941](https://github.com/etimmons24/python-challenge-1/assets/163076822/d13560fd-4d51-4790-a405-bb194742f2ac)

![Screenshot 2024-04-02 114851](https://github.com/etimmons24/python-challenge-1/assets/163076822/8d11d2cf-bf03-4ba7-b1e9-afe394fc0f84)

![Screenshot 2024-04-02 114925](https://github.com/etimmons24/python-challenge-1/assets/163076822/21e25d93-c375-4d09-9713-2d9996310970)

![Screenshot 2024-04-02 114955](https://github.com/etimmons24/python-challenge-1/assets/163076822/d7bee861-abdd-40b1-9339-36beb83f5072)


Please submit bug reports and feature suggestions, or track changes in the [issue queue].

## Requirements:

### Order System 
An order list is initialized.

User is prompted for their menu item selection and it's saved as a variable menu_selection. 

User input menu_selection is checked as a number and an error is printed if it is not. 

menu_selection is converted to an integer.

An if-else statement is used to check if menu_selection is in the menu_items keys, and an error is printed if it isn't.

The item name of the customer's selection is extracted from the menu_items dictionary and stored as a variable.

The customer is prompted for a quantity of their item selection and the value defaults to 1 if the customer does not input a valid number.

The customer's selected item, price, and quantity are appended to the order list in dictionary format.

A match-case statement is used to check if the customer would like to keep ordering, and performs the correct actions for y, n, and default cases.

The match-case statement converts the use input to lowercase or uppercase before checking the case.

### Order Receipt 
A for loop is used to loop through the order list.

The value of each key in each order dictionary is saved as a variable.

The number of formatting spaces are correctly calculated.

Space strings are created using string multiplication.

The customer's order is printed with the item name, price, and quantity.

List comprehension is used to calculate the total price of the order.

The total price of the order is printed to the screen. 
