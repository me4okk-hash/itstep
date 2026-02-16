# Задание 1

# numbers = input("Введiть числа через пробiл: ").split()
# num = []

# for i in numbers:
#     num.append(int(i))

# total = 0
# for i in num:
#     total += i

# result = total / len(num)

# print(f"Результат: {total}, {result}")

# Задание 2

# collection = input("Введiть елементи списку через пробiл: ").split()
# num = []

# for i in collection:
#     num.append(int(i))

# search = int(input("Число для пошуку: "))

# counter = 0
# for i in num:
#     if i == search:
#         counter += 1

# print(f"кількість: {counter}")

# Задание 3

# collection = input("Введiть список чисел через пробiл: ").split()
# num = []

# for i in collection:
#     num.append(int(i))

# positive_sum = 0
# for i in num:
#     if i > 0:
#         positive_sum += i

# print(f"Сума додатних чисел: {positive_sum}")

# Задание 4

# collection = input("Введiть список цiлих чисел через пробiл: ").split()
# num = []

# for i in collection:
#     num.append(int(i))

# index = []

# for i in range(len(num)):
#     if num[i] % 2 == 0:
#         index.append(i)

# print(f"Індекси парних чисел: {index}")

# Задание 5

# collection = input("Введiть список цiлих чисел через пробiл: ").split()
# num = []

# for i in collection:
#     num.append(int(i))

# unique = []

# for i in num:
#     if num.count(i) == 1:
#         unique.append(i)

# print(f"Унікальні: {unique}")