#  Задание 1
# start = int(input("початок діапазону: "))
# end = int(input("кінець діапазону: "))
# number = start         

# while number <= end:
#  if number % 7 == 0:
#   print(number)
#  number += 1

#  Задание 2

# start = int(input("початок діапазону: ")) 
# end = int(input("кінець діапазону: "))
# number = start

# print("Усі числа діапазону:")
# while number <= end:
#     number += 1
#     print(number)

# print("Усі числа діапазону в спадному порядку:")
# number = end
# while number >= start:
#     number -= 1
#     print(number)

# print("Усі числа, кратні 7:")
# number = start
# while number <= end:
#     if number % 7 == 0:
#         print(number)
#     number += 1

# print("Кількість чисел, кратних 5:")
# count_5 = 0
# number = start
# while number <= end:
#     if number % 5 == 0:
#         count_5 += 1
#     number += 1
# print(count_5)

#  Задание 3

# start = int(input("початок діапазону: "))
# end = int(input("кінець діапазону: "))
# number = start 


# while number <= end:
#     if number % 3 == 0 and number % 5 == 0:
#         print("Fizz Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
#     number += 1

# Задание 4

# start = int(input("початок діапазону: "))
# end = int(input("кінець діапазону: ")) 
# step = int(input("крок: "))
# choice = input("виберіть порядок прямий, зворотній: ")
# number = start

# if choice == "прямий":
#     while number <= end:
#         print(number)
#         number += step
# elif choice == "зворотній":
#     number = end
#     while number >= start:
#         print(number)
#         number -= step

# Задание 5

# start = int(input("початок діапазону: "))
# end = int(input("кінець діапазону: "))
# number = start
# product = None

# while number <= end:
#     if number % 4 == 0 and number % 6 != 0:
#         if product is None:
#             product = number
#         else:
#             product *= number
#     number += 1
# if product is None:
#     print(product)
# else:
#     print("таких чисел немає")

# Задание 6

# num1 = (int(input("Введіть перше число: ")))
# num2 = (int(input("Введіть друге число: ")))
# result = 1
# count = 0 

# while count < num2:
#     result *= num1
#     count += 1
# print(result)