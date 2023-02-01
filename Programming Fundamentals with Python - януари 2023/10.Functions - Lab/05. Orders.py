def calculate_price(product, quantity):
    prices = {
        "coffee": 1.50,
        "water": 1.00,
        "coke": 1.40,
        "snacks": 2.00
    }
    return f"{prices[product] * quantity:.2f}"


product = input()
quantity = int(input())

print(calculate_price(product, quantity))