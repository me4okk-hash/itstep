# Задание 1
# symbol = input("Введіть символ: ")

# width = int(input("Введіть ширину: "))
# height = int(input("Введіть висоту: "))
# for i in range(height):
#     print(symbol * width)

# Задание 2

# figure = input("Виберiть фігуру (квадрат, прямокутник): ")
# symbol = input("Введіть символ яким фiгура буде заповнена: ")

# if figure == "квадрат":
#     side = int(input("Введіть довжину сторони квадрата: "))
#     for i in range(side):
#         print(symbol * side)
# elif figure == "прямокутник":
#     width = int(input("Введіть ширину прямокутника: "))
#     height = int(input("Введіть висоту прямокутника: "))
#     for i in range(height):
#         print(symbol * width)

# Задание 3

# size = int(input("Введіть розмір квадрату: "))

# for i in range(size):
#    for j in range(size): 
#         if i == 0 or i == size - 1 or j == 0 or j == size - 1:      
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#    print()

# Задание 4

# width = int(input("Введіть ширину прямокутника: "))
# height = int(input("Введіть висоту прямокутника: "))

# for i in range(height):
#    for j in range(width): 
#         if i == 0 or i == height - 1 or j == 0 or j == width - 1:      
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#    print()

# Задание 5

# height = int(input("Введіть висоту трикутника: "))
# symbol = input("Введіть символ яким буде заповнений трикутник: ")

# for i in range(1, height + 1):
#     print(symbol * i)

# Задание 6

# height = int(input("Введіть висоту трикутника: "))
# symbol = input("Введіть символ яким буде заповнений трикутник: ")

# for i in range(1, height + 1):
#     spaces = height - i
#     symbols = 2 * i - 1
#     print(" " * spaces + symbol * symbols)