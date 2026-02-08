# Задание 1
# inp = input("Введiть рядок: ")

# letter = 0
# numbers = 0

# for i in range(len(inp)):
#     if inp[i].isalpha():
#         letter += 1
#     elif inp[i].isdigit():
#         numbers += 1

# print(f"Кількість букв: {letter}")
# print(f"Кількість цифр: {numbers}")

# Задание 2

# inp = input("Введiть рядок: ")
# find_symbol = input("Введiть символ для пошуку: ")
# counter = 0 

# for i in range(len(inp)):
#     if inp[i] == find_symbol:
#         counter += 1
# print(f"Знайдено символів '{find_symbol}': {counter}")

# Задание 3

# inp = input("Введiть рядок: ")

# text_turn = ""
# for i in range(len(inp) - 1, -1, -1):
#     text_turn += inp[i]
# print(text_turn)

# Задание 4

# inp = input("Введiть рядок: ")
# find_word = input("Введiть слово для пошуку: ")
# counter = 0

# for i in range(len(inp) - len(find_word) + 1):
#     if inp[i:i+len(find_word)] == find_word:
#         counter += 1
# print(f"Знайдено слов '{find_word}': {counter}")

# Задание 5

# inp = input("Введiть рядок: ")
# find_word = input("Введiть слово для пошуку: ")
# replace_word = input("Введiть слово для заміни: ")

# modified_string = inp.replace(find_word, replace_word)

# print(f"Результат: {modified_string}")

# Задание 6

inp = input("Введiть рядок: ")
words = inp.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)
