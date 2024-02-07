# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# Inventory Menu (nested dictionary)
inventory = {
    'cold': {
        'a': "Tea",
        'b': "Coke",
        'c': "7Up",
        'd': "Milk",
    },
    'hot': {
        'a': "Tea",
        'b': "Cocoa",
        'c': "Coffee",
        'd': "Onion Soup",
        'e': "Corn Soup",
    },
    'food': {
        'a': "Sandwich",
        'b': "Salad",
        'c': "Chicken Soup",
        'd': "All-Organic lunch",
    },
    'snacks': {
        'a': "Chocolat Bar",
        'b': "Cookies",
        'c': "Chips",
        'd': "All-Organic Healthy Snak",
    }
}


def get_menu_main(inventory):
    menu: list = ["------"]
    for option, category in enumerate(inventory, start=1):
        menu.append( f"{option} - {category.capitalize()}" )

    menu.append("?: ")
    return "\n".join(menu)


def vending_machine(item):
    print(f"Sorry, we're currently out of {item}. Apologies for the inconvenience.")

def verify(inventory):
    while True:
        try:
            choice = int(input(get_menu_main(inventory)))
            if 1 <= choice <= len(inventory):
                return list(inventory.keys())[choice - 1]
            else:
                print("You pressed the wrong button! Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def verify(choice, inventory):
    while True:
        try:
            choice = int(choice)
            if 1 <= choice <= len(inventory):
                return list(inventory.keys())[choice - 1]
            else:
                print("You pressed the wrong button! Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")




def main():
    msg = "Welcome to SMC Python vending machine. Press a the corresponding button to order"
    global inventory

    choice = verify(inventory)
    vending_machine(choice)

if __name__ == "__main__":
    main()
