# Задание 1
# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))
# num3 = float(input("Введите третье число: "))
# operation = input("Введите операцию (+, -): ")

# if operation == "+":
#     print(f"{num1} + {num2} + {num3} = {num1 + num2 + num3}")
# elif operation == "-":
#     print(f"{num1} - {num2} - {num3} = {num1 - num2 - num3}")
# else:
#     print("Выберите операцию из списка пожалуйста!")

# Задание 2

# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))
# num3 = float(input("Введите третье число: "))

# print("\nВыберите операцию:")
# print("1 - Найти максимум")
# print("2 - Найти минимум")
# print("3 - Найти среднее арифметическое")

# choice = input("Выберите операцию (1-3): ")

# if choice == "1":
#     print(f"Максимум : {max(num1, num2, num3)}")
# elif choice == "2":
#     print(f"Минимум : {min(num1, num2, num3)}")
# elif choice == "3":
#     print(f"Среднее арифметическое : {(num1 + num2 + num3) / 3}")
# else:
#     print("Неправильная операция")


# Задание 3 

# grade = float(input("Введите вашу оценку (1-5): "))
# if grade == 1:
#     print("Дуже погано.")
# elif grade == 2:
#     print("Погано.")
# elif grade == 3:
#     print("Задовільно.")
# elif grade == 4:
#     print("Добре.")
# elif grade == 5:
#     print("Відмінно.")
# else:
#     print("У нас пятибальная система")


# Задание 4

# meters = float(input("Введите количество метров: "))
# miles = meters * 0.000621371
# inches = meters * 39.3701
# yard = meters * 1.09361
# km = meters / 1000
# cm = meters * 100

# print("\nВыберите вариант конвертации:")
# print("1 - Перевести в мили")
# print("2 - Перевести в дюймы")
# print("3 - Перевести в ярды")
# print("4 - Перевести во все три единицы (мили, дюймы, ярды)")
# print("5 - Перевести в километры и сантиметры")

# choice = input("Введите то во что хотите перевести (1-5): ")

# if choice == "1":
#     print(f"{meters} метров = {miles} миль")
# elif choice == "2":
#     print(f"{meters} метров = {inches} дюймов")
# elif choice == "3":
#     print(f"{meters} метров = {yard} ярдов")
# elif choice == "4":
#     print(f"{meters} метров = {miles} миль, {inches} дюймов, {yard} ярдов")
# elif choice == "5":
#     print(f"{meters} метров = {km} километров, {cm} сантиметров")


# Задание 5

# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))
# operation = input("Введите операцию (+, -, *, /, %, **): ")

# if operation == "+":
#     print(f"{num1} + {num2} = {num1 + num2}")
# elif operation == "-":
#     print(f"{num1} - {num2} = {num1 - num2}")  
# elif operation == "*":
#     print(f"{num1} * {num2} = {num1 * num2}")
# elif operation == "%":
#     print(f"{num2}% от {num1} = {(num1 * num2) / 100}")
# elif operation == "**":
#     print(f"{num1} ** {num2} = {num1 ** num2}")
# elif operation == "/":
#     if num2 == 0:
#         print("На ноль делить нельзя")
#     else:
#         print(f"{num1} / {num2} = {num1 / num2}")
# else:
#     print("Некоректная операция")


# Задание 6

# number = input("Введите трёхзначное число: ")
# a, b, c = number

# if a == b == c:
#     print("Все цифры одинаковые")
# else:
#     print("Все цифры разные")