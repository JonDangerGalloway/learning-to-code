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

coins = {
    "quarters": .25,
    "dimes": .10,
    "nickels": .05,
    "pennies": .01,
}
def make_payment():
    amount_paid = 0
    for item in coins:
        coin_value = (coins[item])
        coin_amount = int(input(f"How many {item}? "))
        total_coin_value = coin_value * coin_amount
        amount_paid += total_coin_value

    return amount_paid


paid = make_payment()
print(paid)
