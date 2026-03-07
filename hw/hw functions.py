# Задание 1 

# def printed():
#     print("\"Don't compare yourself with anyone in this world...")
#     print("     if you do so, you are insulting yourself.\"")
#     print("         Bill Gates")

# printed()

# Задание 2

# def even_nums(a, b):
#      for i in range(a, b + 1):
#         if i % 2 == 0:
#             print(i)
    
# a1 = int(input("Введіть перше число: "))
# b1 = int(input("Введіть друге число: "))
# even_nums(a1, b1)

# Задание 3

# def square(size, symbol, filling):
#     for i in range(size):
#         if filling:
#             print(symbol * size)
#         else:
#             if i == 0 or i == size - 1:
#                 print(symbol * size)
#             else:
#                 print(symbol + " " * (size - 2) + symbol)
    
# square_size = int(input("Введіть розмір квадрата: "))
# square_symbol = input("Введіть символ для квадрата: ")
# square_filling = input("Чи заповнений квадрат? (true/false): ").lower() == "true"
# square(square_size, square_symbol, square_filling)

# Задание 4

# def amount_of_digits(num):
#     return len(str(num))

# input = int(input("Введіть число: "))
# print(amount_of_digits(input))

# Задание 5

def is_palindrome(number):
    clean_string = str(number).replace(" ", "").lower()
    return clean_string == clean_string[::-1]

input_number = int(input("Введіть число: "))
if is_palindrome(input_number):
    print("Це паліндром")
else:   
    print("Це не паліндром")