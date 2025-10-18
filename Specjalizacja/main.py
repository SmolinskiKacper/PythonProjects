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
    "money" : 0,
}
def make_coffe(prompt):
    total = 0
    if prompt == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {resources['money']}")
    if prompt != "report":
        print("Please insert coins")
        total += int(input("how many quarters ")) * 0.25
        total += int(input("how many dimes ")) * 0.10
        total += int(input("how many nickles ")) * 0.05
        total += int(input("how many pennies ")) * 0.01

    drink =MENU[prompt]

    if total < drink["cost"]:
        print("Not enough money")
        print(total)
        return

    for item, amount in drink["ingredients"].items():
        if resources[item] < amount:
            print(f"Sorry, not enough {item}")
            return

    for item, amount in drink["ingredients"].items():
        resources[item] -= amount             #resources[item] -= drink["ingredients"][item]

    resources["money"] += drink["cost"]
    change = round(total - drink["cost"], 2)
    print(f"Here's your change: ${change:.2f}")

on = True
while on:
    prompt = input("What would you like? (espresso/latte/cappuccino):")
    if prompt == "off":
        on = False
    else:
        make_coffe(prompt)


    # if prompt == "espresso" and total >= MENU["espresso"]["cost"]:
    #     if resources["water"] >= MENU["espresso"]["ingredients"]['water'] and resources["coffee"] >= MENU["espresso"]["ingredients"]['coffee']:
    #         resources["water"] -= MENU["espresso"]["ingredients"]['water']
    #         resources["coffee"] -= MENU["espresso"]["ingredients"]['coffee']
    #         resources["money"] += 1.5
    #         change = round(total - MENU["espresso"]["cost"],2)
    #         print(f"Here's your change: {change}")
    #     else:
    #         print("not enough resources")
    # elif prompt == "espresso" and total < MENU["espresso"]["cost"]:
    #         print("Not enough money")
    #
    #
    # if prompt == "latte" and total >= MENU["latte"]["cost"]:
    #     if resources["water"] >= MENU["latte"]["ingredients"]['water'] and resources["milk"] >= MENU["latte"]["ingredients"]['milk'] and resources["coffee"] >= MENU["latte"]["ingredients"]['coffee']:
    #         resources["water"] -= MENU["latte"]["ingredients"]['water']
    #         resources["milk"] -= MENU["latte"]["ingredients"]['milk']
    #         resources["coffee"] -= MENU["latte"]["ingredients"]['coffee']
    #         resources["money"] += 2.5
    #         change = round(total - MENU["latte"]["cost"],2)
    #         print(f"Here's your change: {change}")
    #     else:
    #         print("not enough resources")
    # elif prompt == "latte" and total < MENU["latte"]["cost"]:
    #     print("Not enough money")
    #
    #
    # if prompt == "cappuccino" and total >= MENU["cappuccino"]["cost"]:
    #     if resources["water"] >= MENU["cappuccino"]["ingredients"]['water'] and resources["milk"] >= MENU["cappuccino"]["ingredients"]['milk'] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]['coffee']:
    #         resources["water"] -= MENU["cappuccino"]["ingredients"]['water']
    #         resources["milk"] -= MENU["cappuccino"]["ingredients"]['milk']
    #         resources["coffee"] -= MENU["cappuccino"]["ingredients"]['coffee']
    #         resources["money"] += 3.0
    #         change = round(total - MENU["cappuccino"]["cost"],2)
    #         print(f"Here's your change: {change}")
    #     else:
    #         print("not enough resources")
    # elif prompt == "cappuccino" and total < MENU["cappuccino"]["cost"]:
    #     print("Not enough money")