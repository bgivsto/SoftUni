chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

chicken_menu_price = chicken_menus * 10.35
fish_menu_price = fish_menus * 12.40
vegetarian_menu_price = vegetarian_menus * 8.15
delivery_price = 2.50
main_meal_price = chicken_menu_price + fish_menu_price + vegetarian_menu_price
desert_price = 0.2 * main_meal_price

total_price = main_meal_price + desert_price + delivery_price

print(f"{total_price:.2f}")
