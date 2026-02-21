# Задание 1 
# user_input = input("Введіть числа через пробіл: ").split()
# numbers = []


# for i in user_input:
#     numbers.append(int(i))

# shift = int(input("На скільки позицій зсунути: "))

# if len(numbers) > 0:
#     shift = shift % len(numbers)
    
#     for i in range(shift):
#         last_item = numbers.pop()
#         numbers.insert(0, last_item)

# print(f"Результат: {numbers}")

# Задание 2
import random

list1 = []
list2 = []
for i in range(10):
    list1.append(random.randint(1, 20))
    list2.append(random.randint(1, 20))

print(f"Список 1: {list1}")
print(f"Список 2: {list2}")

combined_list = list1 + list2
print(f"Елементи обох: {combined_list}")

no_duplicates = []
for item in combined_list:
    if item not in no_duplicates:
        no_duplicates.append(item)
print(f"Без повторень: {no_duplicates}")

common = []
for item in list1:
    if item in list2 and item not in common:
        common.append(item)
print(f"Спільні: {common}")

unique_only = []
for item in list1:
    if item not in list2 and item not in unique_only:
        unique_only.append(item)
for item in list2:
    if item not in list1 and item not in unique_only:
        unique_only.append(item)
print(f"Унікальні для кожного: {unique_only}")

min1 = list1[0]
max1 = list1[0]
for item in list1:
    if item < min1: min1 = item
    if item > max1: max1 = item

min2 = list2[0]
max2 = list2[0]
for item in list2:
    if item < min2: min2 = item
    if item > max2: max2 = item

extremes = [min1, max1, min2, max2]
print(f"Min/Max: {extremes}")