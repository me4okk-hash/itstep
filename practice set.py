import random

# Задание 1
# num_set = [1, 2, 2, 3, 4, 4, 5]
# print(set(num_set))

# Задание 2

# num_set1 = set()
# num_set2 = set()

# for i in range(10):
#     num_set1.add(random.randint(1, 20))
#     num_set2.add(random.randint(1, 20))

# print(f"множина 1: {num_set1} ")
# print(f"множина 2: {num_set2}")
# print(f"спільні: {num_set1 & num_set2}")
# print(f"різниця: {num_set1 - num_set2}")
# print(f"об’єднання: {num_set1 | num_set2}")

# Задание 3

word1 = input("Введіть перше слово: ") 
word2 = input("Введіть друге слово: ")

if set(word1) == set(word2):
    print("анаграма")
else:
    print("не анаграма")
