# # def get_discounted_prices(prices: list):
# #     discounted_prices = []
# #     for price in prices:
# #         if price > 100:
# #             discounted_prices.append(price * 0.8)

# #     return discounted_prices

# # original_prices = [50, 120, 80, 200, 300]
# # result = get_discounted_prices(original_prices)
# # print(result)

# def recursion():
#     print("recursion")
#     recursion()

# # def func_b():
# #     print("func_b")
# #     func_a()

# # def func_a():
# #     print("func_a")
# #     func_b()

# # Факториал числа !5 = 1 * 2 * 3 * 4 * 5 = 120

# def factorial_loop(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# # print(factorial_loop(5))

# def factorial_recursion(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial_recursion(n - 1)
    
# # print(factorial_recursion(5))

# # def say_hello():
# #     print("Hello!")

# # func_var = say_hello

# # def some_function(callback):
# #     print("some+func calls its callback")
# #     callback()

# # def log_file(message):
# #     pass

# # def log_console(message):
# #     pass

# # def log_database(message):
# #     pass

# # def do_some_work(log_callback):
# #     print("Doing something...")
# #     log_callback("Done!")
# #     log_callback("logging message")






# # do_some_work(log_console)
# # do_some_work(log_database)
# # do_some_work(log_file)

# # func_var()
# # print(type(func_var))

# sum = lambda a, b: a + b

# # print(sum(10, 12))

# operations = {
#     '+': lambda a, b: a + b,
#     '-': lambda a, b: a - b,
#     '*': lambda a, b: a * b,
# }

# # num1 = float(input("Введіть перше число: "))
# # num2 = float(input("Введіть друге число: "))
# # action = input("Введіть оператор (+, -, *): ")

# # if action in operations:
# #     print(operations[action](num1, num2))
# # else:    
# #     print("Невірний оператор")

# tax_rate = 0.5

# def calculate_tax_impure(amount):
#     return amount * tax_rate

# # print(calculate_tax_impure(10000))

# def calculate_tax_pure(amount, tax_rate):
#     return amount * tax_rate

# # print(calculate_tax_pure(10000, 0.3))

# def add_product_impure(cart: list, product: str):
#     cart.append(product)
#     return cart

# def add_product_pure(cart: list, product: str):
#     new_cart = cart.copy()
#     new_cart.append(product)
#     return new_cart

# my_cart = ['apple', 'banana']
# # add_product_impure(my_cart, 'orange')
# new_cart = add_product_pure(my_cart, 'orange')

# print(my_cart)

# my_set_1 = {'apple', 'orange'}
# my_set_2 = {'pear', 'banana'}

# union = my_set_1.union(my_set_2)
# print(union)
# print(my_set_1)


def create_multiplier(factor):
    def multiplier(num):
        return num * factor
    return multiplier

doubler = create_multiplier(2)
tripler = create_multiplier(3)

print(doubler(4))
print(tripler(10))