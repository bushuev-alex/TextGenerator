menu = {'pizza': 'Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy',
        'salad': 'Caesar salad, Green salad, Tuna salad, Fruit salad',
        'soup': 'Chicken soup, Ramen, Tomato soup, Mushroom cream soup'}

my_choice = input()

if my_choice in menu.keys():
    print(menu[my_choice])
else:
    print("Sorry, we don't have it in the menu")
