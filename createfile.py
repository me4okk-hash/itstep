# Задание 1
# file_path = "data.txt"
# backup_path = "backup.txt"

# def read():
#     try:
#         with open(file_path, "r") as a:
#             return a.readlines()
#     except FileNotFoundError:
#         print("Файл не знайдено")

#         # створюємо файл
#         with open(file_path, "a"):
#             pass

#         return []


# def write(lines):
#     with open(backup_path, "w") as i:
#         i.writelines(lines)

# lines = read()
# write(lines)

# Задание 2

# file_path = "data.txt"
# encrypted_path = "encrypted.txt"

# with open(file_path, "a"):
#     pass

# def next_letter(char):
#     if char == 'z':
#         return 'a'
#     elif char == 'Z':
#         return 'A'
#     elif char.isalpha():
#         return chr(ord(char) + 1)
#     else:
#         return char
    

# def read():
#     with open(file_path, "r") as file:
#         return file.read()
    

# def write(text):
#     with open(encrypted_path, "w") as file:
#         file.write(text)

# text = read()
# result = ""
# for char in text:
#     result += next_letter(char)

# write(result)

# Задание 3

file_path = 'music_collection.txt'

with open(file_path, 'a'):
    pass


def add_album():
    title = input('Введiть назву: ')
    artist = input('Введiть виконавця: ')
    year = input('Введiть рiк: ')

    with open(file_path, 'a') as file:
        file.write(title + ',' + artist + ',' + year + "\n")


def show_all():
    with open(file_path, 'r') as file:
        for line in file:
            print(line.strip())


def search():
    artist_name = input('Введiть виконавця: ')

    with open(file_path, 'r') as file:
        for line in file:
            if artist_name.lower() in line.lower():
                print(line.strip())


def delete():
    title_name = input('Введiть назву: ')
    new_lines = []

    with open(file_path, 'r') as file:
        for line in file:
            if title_name.lower() not in line.lower():
                new_lines.append(line)

    with open(file_path, 'w') as f:
        f.writelines(new_lines)


while True:
    print("\n1 - Додати")
    print("2 - Показати")
    print("3 - Пошук")
    print("4 - Видалити")
    print("5 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        add_album()
    elif choice == "2":
        show_all()
    elif choice == "3":
        search()
    elif choice == "4":
        delete()
    elif choice == "5":
        break
