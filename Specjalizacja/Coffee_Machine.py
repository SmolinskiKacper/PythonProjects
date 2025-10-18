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
