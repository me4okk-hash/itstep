# Задание 1
# string = input("Введіть рядок: ")
# counter = 0

# for i in range(len(string)):
#     if string[i] == "." or string[i] == "!" or string[i] == "?":
#         if i == len(string) - 1:
#             counter += 1
#         elif string[i+1] != "." and string[i+1] != "!" and string[i+1] != "?":
#             counter += 1

# print(f"Кількість речень: {counter}")

# Задание 2

# string = input("Введіть рядок: ")
# clean_string= ""

# for char in string:
#     if char != " ":
#         clean_string += char.lower()

# if clean_string == clean_string[::-1]:
#     print("Це паліндром")
# else:
#     print("Це не паліндром")


# Задание 3

# string = input("Введіть текст: ")
# reserved = "python", "код", "завдання"
# words = string.split()
# result_text = ""


# for word in words:
#     clean_word = word.lower().strip(".,!?")
    
#     if clean_word in reserved:
#         result_text = result_text + word.upper() + " "
#     else:
#         result_text = result_text + word + " "

# print(result_text.strip())

# Задание 4

# string = input("Введiть рядок: ")
# symbol_1 = input("Введiть перший символ: ")
# symbol_2 = input("Введiть другий символ: ")
# part_1 = string.split(symbol_1)[0]
# part_2 = string.split(symbol_2)[-1]

# print(part_1 + part_2)

# Задание 5

string = input("Введіть текст: ")
symbol = input("Введіть символи: ")
words = string.split()
result = " "

for word in words:
    delete = False
    for i in symbol:
        if i in word:
            delete = True

    if delete == False:
        result = result + word + " "

print(f"Результат: {result}")

# Задание 6
# string = input("Введiть рядок: ")
# words = string.split()
# result = ""

# for word in words[::-1]:
#     if result:
#         result += " "
#     result += word

# print(result)
