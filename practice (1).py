# Задание 1 

# a = int(input("Введіть число: "))

# for i in range(1, 11):
#     print(f"{a} * {i} = {a * i}")

# Задание 2 

# for i in range(1, 10):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}")

# Задание 3 

# n = int(input("Введіть скільки чисел ви хочете ввести: "))
# max_number = None

# for i in range(n):
#     number = int(input(f"Введіть число {i + 1}: "))
#     if max_number is None or number > max_number:
#         max_number = number
# print("Найбільше число:", max_number) 

# Задание 4

# import random

# generated_number = random.randint(1, 500)
# attempt = 0

# while True:
#     input_number = int(input("Введіть число від 1-500: "))
#     if input_number == 0:
#         break

#     attempt += 1

#     if input_number < generated_number:
#         print("число більше ")
#         continue
#     elif input_number > generated_number:
#         print("число меньше")
    
#     elif input_number == generated_number:
#         print(f"число було {generated_number}")
#         print(f"вгадано за {attempt}")
#         break

# Задание 5

# shape = input("Введіть форму (квадрат, прямокутник): ")
# symbol = input("Введіть символ яким фiгура буде намальована: ")

# if shape == "квадрат":
#     side = int(input("Введіть довжину сторони квадрата: "))
#     for i in range(side):
#         print(symbol * side)
# elif shape == "прямокутник":
#     width = int(input("Введіть ширину прямокутника: "))
#     height = int(input("Введіть висоту прямокутника: "))
#     for i in range(height):
#         print(symbol * width) 
# else:
#     print("error")