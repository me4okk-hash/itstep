# Задание 1

# def formatted_print():
#     print("\"Don't let the noise of others' opinions")
#     print("     drown out your own inner voice.\"")
#     print("         Steve Jobs")

# formatted_print()

# Задание 2

# def print_nums(a, b):
#     for i in range(a, b + 1):
#         if i % 2 == 0:
#             print(i)

# start = int(input("Введіть початкове число: "))
# end = int(input("Введіть кінцеве число: "))
# print_nums(start, end)

# Задание 3

# def show_line(length, direction, symbol):
#     if direction == 'h':
#         for _ in range(length):
#             print(symbol, end="")
#         print()
#     elif direction == 'v':
#         for _ in range(length):
#             print(symbol)
#     else:
#         print("Помилка використовуйте 'h' для горизонтальної лінії або 'v' для вертикальної лінії.")

# line_length = int(input("Введіть довжину лінії: "))
# line_direction = input("Введіть напрямок лінії (h для горизонтальної, v для вертикальної): ")
# line_symbol = input("Введіть символ для лінії: ")
# show_line(line_length, line_direction, line_symbol)

# Задание 4

# def max_of_four(a, b, c, d):
#     return max(a, b, c, d)

# max_from_four = (input("Введіть чотири числа через пробіл: ").split())
# max_four = (max_from_four[0], max_from_four[1], max_from_four[2], max_from_four[3])
# print(max_of_four(int(max_four[0]), int(max_four[1]), int(max_four[2]), int(max_four[3])))

# Задание 5

# def is_num_easy(num):
#      if num % 2 == 0:
#          return True
#      else:
#          return False
    
# easy_input = int(input("Введіть число: "))
# is_easy = is_num_easy(easy_input)
# print(is_easy)

# Задание 6

# def is_num_lucky(num):
#     num = str(num)
#     if len(num) != 6:
#         return False
#     p1 = int(num[0]) + int(num[1]) + int(num[2])
#     p2 = int(num[3]) + int(num[4]) + int(num[5])
#     if p1 == p2:
#         return True
#     else:
#         return False
    
# lucky_num = int(input("Введіть шестизначне число: "))
# is_lucky = is_num_lucky(lucky_num)