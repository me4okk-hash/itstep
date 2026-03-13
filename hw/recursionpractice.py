import random
# Задание 1
 
# def power(num, exp):
#     if exp == 0:
#         return 1
#     elif exp > 0:
#         return num * power(num, exp - 1)
#     else:
#         return 1 / power(num, -exp)

# num1 = int(input("Введіть число: "))
# num2 = int(input("Введіть степінь: "))
# print(power(num1, num2)) 

# Задание 2

# def leap(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# def days_month(year, month):
#     if month in [4, 6, 9, 11]:
#         return 30
#     elif month == 2:
#         return 29 if leap(year) else 28
#     else:
#         return 31


# def absolute(number):
#     return number if number >= 0 else -number


# def date_to_absolute_date(day, month, year):
#     total_days = day

#     for y in range(1, year):
#         total_days += 366 if leap(y) else 365

#     for m in range(1, month):
#         total_days += days_month(year, m)

#     return total_days


# def days_diff(day1, month1, year1, day2, month2, year2):

#     absolute_date1 = date_to_absolute_date(day1, month1, year1)
#     absolute_date2 = date_to_absolute_date(day2, month2, year2)

#     return absolute(absolute_date1 - absolute_date2)


# result = days_diff(1, 1, 2026, 2, 1, 2026)
# print(f'Рiзниця {result} день(iв)')

# Задание 3

numbers = [random.randint(1, 100) for _ in range(100)]

def search_min(index):
    if index == len(numbers) - 10:
        return index, float("inf")
    
    current_min = sum(numbers[index:index + 10])

    next_index, next_min = search_min(index + 1)

    if current_min < next_min:
        return index, current_min
    else:
        return next_index, next_min
    
biggest_index, min_sum = search_min(0)
print(f"Індекс першого елемента з найменшою сумою {biggest_index} сума {min_sum}")