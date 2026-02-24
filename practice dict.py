# Задание 1 

# contacts = {}

# while True:
#     print("1. Додати контакт")
#     print("2. Видалити контакт")
#     print("3. Переглянути контакти")
#     print("4. Вийти")

#     choice = input("Виберiть дiю: ")

#     if choice == "1":
#         name = input("Введiть iм'я контакту: ")
#         phone = input("Введiть номер телефону: ")
#         contacts[name] = phone
#         print(f"Контакт {name} додано.")

#     elif choice == "2":
#         name = input("Введiть iм'я контакту для видалення: ")
#         if name in contacts:
#             del contacts[name]
#             print(f"Контакт {name} видалено.")
#         else:
#             print(f"Контакт {name} не знайдено")

#     elif choice == "3":
#         if contacts:
#             for name, phone in contacts.items():
#                 print(f"{name}: {phone}")
#         else:
#             print("Контакти вiдсутнi.")

#     elif choice == "4":
#         break

#     else:
#         print("Невiрний вибiр. Спробуйте ще раз.")

# Задание 2

# input_text = input("Введiть текст: ").lower() 
# words = input_text.split()
# word_count = {}

# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1
# print("Кiлькiсть слов")
# for word in word_count:
#     print(f"{word}: {word_count[word]}")

# Задание 3

# rate = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}
# uah = float(input("Введiть суму в гривнях: "))
# currency = input("Введiть валюту (USD, EUR, PLN): ").upper()

# if currency in rate:
#     print(f"{uah} UAH = {uah / rate[currency]} {currency}")
# else:
#     print("Такої валюти немає")

# Задание 4

# translate = {"hello": "Привiт", "how are you?": "Як справи?", "goodbye": "До побачення"}
# word = input("Введiть слово для перекладу: ").lower().strip()

# if word in translate:
#     print(f"Переклад: {translate[word]}")
# else:    
#     print("Слово не знайдено в словнику.")