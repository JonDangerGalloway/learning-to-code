from resources import MENU, ingredients, coins


def make_payment():
    payment = 0
    print("Please insert coins.")
    for item in coins:
        coin_value = (coins[item])
        coin_amount = int(input(f"How many {item}? "))
        total_coin_value = coin_value * coin_amount
        payment += total_coin_value
    return payment


def cost(coffee_type):
    selection_cost = MENU[coffee_type]["cost"]
    return selection_cost


def check_ingredients(coffee_type):
    chosen_drink_ingredients = MENU[coffee_type]["ingredients"]
    available_machine_ingredients = ingredients
    for item in available_machine_ingredients:
        if item in chosen_drink_ingredients:
            machine_ingredients = (available_machine_ingredients[item])
            recipe_requirements = (chosen_drink_ingredients[item])
            if machine_ingredients < recipe_requirements:
                print(f"Sorry, there is not enough {item}")
                return "out"

            else:
                machine_amount_left = machine_ingredients - recipe_requirements
                available_machine_ingredients[item] = machine_amount_left
    return ingredients


def run_report():
    print(f"Water: {ingredients['water']}ml")
    print(f"Milk: {ingredients['milk']}ml")
    print(f"Coffee: {ingredients['coffee']}g")
    print(f"Money: ${profit}")


profit = 0
run_machine = True
while run_machine:
    type_of_coffee = input("What would you like? (espresso/latte/cappuccino)\n").lower()

    if type_of_coffee == "off":
        run_machine = False

    elif type_of_coffee == "report":
        print(run_report())

    else:
        any_left = check_ingredients(type_of_coffee)
        if any_left == "out":
            run_machine = True
        else:
            coffee_cost = (cost(type_of_coffee))
            profit += coffee_cost
            amount_paid = make_payment()
            change = amount_paid - coffee_cost
            if amount_paid < coffee_cost:
                print("Sorry, that's not enough money. Money refunded")
            elif amount_paid == coffee_cost:
                print(f"Here is your {type_of_coffee}, enjoy!")
            else:
                print(f"Your change is ${round(change, 2)}")
                print(f"Here is your {type_of_coffee}, enjoy!")
