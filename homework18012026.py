# Задание 1 
# number = float(input("Введите число: "))
# degree = int(input("Выберите степень от 0 до 7: "))

# match degree:
#     case 0: print(f"{number} =", 1)
#     case 1: print(f"{number} =", number)
#     case 2: print(f"{number} =", number * number)
#     case 3: print(f"{number} =", number * number * number)
#     case 4: print(f"{number} =", number * number * number * number)
#     case 5: print(f"{number} =", number ** 5)
#     case 6: print(f"{number} =", number ** 6)
#     case 7: print(f"{number} =", number ** 7)
#     case _: print("Можна обрати ступінь тiльки від 0 до 7")

# Задание 2

# number = int(input("Введiть число вiд 1 до 100: "))

# if 1 <= number <= 100:
#     if number % 3 == 0 and number % 5 == 0:
#         print("Fizz Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
# else:
#     print("Помилка число має бути вiд 1 до 100")

# Задание 3

# snack = input("Виберіть закуску (Салат, Суп, нічого): ")
# main_dish = input("Виберіть основну страву (Курка, Риба, нічого): ")
# dessert = input("Виберіть десерт (Морозиво, Фрукти, нічого): ")
# status = input("Ви постійний клієнт? (так, ні): ")

# price = 0.0
# drink = "немає"
# discount = 0

# match snack:
#     case "Салат": price = price + 5
#     case "Суп": price = price + 7

# match main_dish:
#     case "Курка": price = price + 10
#     case "Риба": price = price + 12

# match dessert:
#     case "Морозиво": price = price + 3
#     case "Фрукти": price = price + 4

# if snack == "Суп" and main_dish == "Риба":
#     if dessert != "нічого":
#         price = price - 2

# if main_dish == "Курка" and dessert == "Морозиво":
#     drink = "Чай"

# if snack != "нічого" and main_dish != "нічого" and dessert != "нічого":
#     discount = 10

# if price > 20:
#     discount = 15

# if status == "так":
#     discount = discount + 5

# total = price - (price * discount / 100)

# print("Базова вартість:", price)
# print("Знижка:", discount, "%")
# print("Безкоштовний напій:", drink)
# print("до сплати:", total)