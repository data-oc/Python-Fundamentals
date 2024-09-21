def hawaiian_pizza(*ingredient):
    for i in ingredient:
        print(i)
    print(type(ingredient))

hawaiian_pizza("cheese", "tomato", "bacon", "pineapple")