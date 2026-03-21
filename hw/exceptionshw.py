import random
# Задание 1

# try:
#     first = float(input("Введiть перше число: "))
#     second = float(input("Введiть перше число: "))
#     result = first / second
#     print (result)

# except ValueError:
#     print("Введено не число")

# except ZeroDivisionError:
#     print("На нуль дiлити не можна")

# finally:
#     print("Операцiя завершена")

# Задание 2

# numbers = [10, 20, 30, 40, 50]

# try:
#     index = int(input("Введiть iндекс елемента: "))
#     print(numbers[index])

# except IndexError:
#     print("Iндекс поза межами списку")

# except ValueError:
#     print("Iндекс має бути числом")

# finally:
#     print("Операцiя завершена")

# Задание 3

# try:
#     data = input("Введiть продажi через пробiл: ")
#     numbers = list(map(float, data.split()))
#     result = sum(numbers)
#     print(f"Загальнi продажi: {result}")

# except ValueError:
#     print("Введено не число")

# finally:
#     print("Операцiя завершена") 

# Задание 4

# try:
#     num = float(input("Введiть число: "))
#     if num < 0:
#         raise Exception("Квадратний корінь не може бути від'ємним")

#     sqrt = num ** 0.5
#     print(f"Квадратний корінь {sqrt}")

# except ValueError:
#     print("Введено не число")

# except Exception as e:
#     print(e)

# finally:
#     print("Обчислення завершено")

# Задание 5

# try:
#     data = input("Введiть товар (назва, ціна, кількість): ")
#     name, price, amount = data.split(",")

#     price = float(price)
#     amount = int(amount)

#     print(f"Товар: {name}, Ціна: {price}, Кількість: {amount}")

# except ValueError:
#     print("Некоректнi данi")

# finally:
#     print("Парсинг завершено")

# Задание 6

def connect_to_server():
    if random.choice([True, False]):
        return "Підключення до серверу успішне"
    else:
        raise ConnectionError("Помилка підключення до серверу")
    
try:
    result = connect_to_server()
    print(result)

except ConnectionError:
    print("Не вдалося підключитися до серверу")

finally:
    print("Спробу завершено")