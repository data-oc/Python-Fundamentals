def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(10, 20, c = 30, d = 40)