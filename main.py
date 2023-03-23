MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_inventory():
    if choose == "latte":
        if resources["water"] >= 200:
            resources["water"] -= 200
        else:
            return f"Sorry there is not enough water."
        if resources["milk"] >= 150:
            resources["milk"] -= 150
        else:
            return f"Sorry there is not enough milk."
        if resources["coffee"] >= 24:
            resources["coffee"] -= 24
        else:
            return f"Sorry there is not enough coffee."
    elif choose == "cappuccino":
        if resources["water"] >= 250:
            resources["water"] -= 250
        else:
            return f"Sorry there is not enough water."
        if resources["coffee"] >= 100:
            resources["coffee"] -= 100
        else:
            return f"Sorry there is not enough coffee."
        if resources["milk"] >= 24:
            resources["milk"] -= 24
        else:
            return f"Sorry there is not enough milk."
    elif choose == "espresso":
        if resources["water"] >= 50:
            resources["water"] -= 50
        else:
            return "Sorry there is not enough water."
        if resources["coffee"] >= 24:
            resources["coffee"] -= 24
        else:
            return f"Sorry there is not enough coffee."

def report(cash):
    resources["money"] = cash
    print(resources)


money = 0

is_on = True
while is_on:
    espresso = 1.5
    latte = 2.5
    cappuccino = 3.0
    choose = input("What would you like? (espresso,latte,cappuccino): ").lower()
    if choose == "off":
        is_on = False
    elif choose == "report":
        report(money)
    elif choose == "espresso" or "cappuccino" or "latte":
        check_inventory()
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        if choose == "latte":
            if total >= latte:
                money += 2.5
                change = round(total - latte, 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your latte. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif choose == "cappuccino":
            if total >= cappuccino:
                money += 3.0
                change = round(total - cappuccino, 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your cappuccino. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif choose == "espresso":
            if total >= espresso:
                money += 1.5
                change = round(total - espresso, 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your espresso. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
