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
money = 0


def user_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    global total_paid
    total_paid = int(0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies)


still_on = True
while still_on:
    user_order = input("What would you like? (espresso/ latte/ cappuccino): ")

    if user_order == "off":
        still_on = False
    elif user_order == "report":
        print(f"Here is your resources: \nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: "
              f"{resources['coffee']}gm\nMoney: ${money}")
    elif user_order == "espresso":
        if resources["water"] > MENU["espresso"]["ingredients"]["water"] and resources["coffee"] > \
                MENU["espresso"]["ingredients"]["coffee"]:
            user_money()
            if total_paid > MENU["espresso"]["cost"]:
                change = total_paid - MENU["espresso"]["cost"]
                money += MENU["espresso"]["cost"]
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                print(f"Here is your change {change}.\nHere is your {user_order}, Enjoy your drink!")
            else:
                print("Not enough money. Try again")
        else:
            print("Not enough resources")
    elif user_order == "latte":
        if resources["water"] > MENU["latte"]["ingredients"]["water"] and resources["coffee"] > \
                MENU["latte"]["ingredients"]["coffee"] and resources["milk"] > MENU["latte"]["ingredients"]["milk"]:
            user_money()
            if total_paid > MENU["latte"]["cost"]:
                change = total_paid - MENU["latte"]["cost"]
                money += MENU["latte"]["cost"]
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                print(f"Here is your change {change}.\nHere is your {user_order}, Enjoy your drink!")
            else:
                print("Not enough money. Try again")
        else:
            print("Not enough resources")
    elif user_order == "cappuccino":
        if resources["water"] > MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"] > \
                MENU["cappuccino"]["ingredients"]["coffee"] and resources["milk"] > MENU["cappuccino"]["ingredients"][
            "milk"]:
            user_money()
            if total_paid > MENU["cappuccino"]["cost"]:
                change = total_paid - MENU["cappuccino"]["cost"]
                money += MENU["cappuccino"]["cost"]
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                print(f"Here is your change {change}.\nHere is your {user_order}, Enjoy your drink!")
            else:
                print("Not enough money. Try again")
        else:
            print("Not enough resources")
