from data import MENU, resources

transaction_ongoing = True
# TODO: 4. Check resources sufficient?


def resource_checker(ingredients):
    transaction_successful = True
    for item in resources:
        if item == "Money":
            continue
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            transaction_successful = False
    return transaction_successful

while transaction_ongoing:
    coins={
        "quarters": 0.25,
        "dime": 0.10,
        "nickel": 0.05,
        "pennies": 0.01
    }
    # TODO: 1.Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

    request = input('What would you like? (espresso/latte/cappuccino):')


    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if request == 'off':
        transaction_ongoing = False

    # TODO: 3. Print report.
    elif request == 'report':
        for resource in resources:
            print(f"{resource} : {resources[resource]}")
    else:
        ingredients = MENU[request]["ingredients"]
        # print(ingredients)
        if not resource_checker(ingredients):
            print("Not enough resources")

        else:
            print("Enough resources")
            # TODO: 5. Process coins.
            for coin in coins:
                coins[coin] = coins[coin] * int(input(f"How many {coin}?:"))
                # print(coins[coin])
            total=round(sum(coins.values()),2)
            # TODO: 6. Check transaction successful?
            price = MENU[request]["cost"]

            if total < price:
                print("Sorry that's not enough money. Money refunded.")
            else:
                for ingredient in resources:
                    if ingredient == "Money":
                        continue
                    resources[ingredient] -= ingredients[ingredient]

                if "Money" in resources:
                    resources["Money"] += price
                else:
                    resources["Money"] = price

                print(f"Here is {total - price} in change")
                print(f"Enjoy your {request}")
