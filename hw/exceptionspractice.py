# Задание 1 

# try:
#     price = float(input("Введiть цiну товару без знижки: "))
#     discount = float(input("Введiть вiдсоток знижки: "))
#     final_price = price * (1 - discount / 100)

#     print(f"Цiна товару з урахуванням знижки: {final_price}")

# except ValueError:
#     print("Ви не ввели число!")

# Задание 2

# try:
#     usd_amount = float(input("Введiть суму в доларах: "))
#     exchange_rate = float(input("Введiть курс обмiну: "))

#     if exchange_rate <= 0 or exchange_rate == 0:
#         raise Exception("Курс обмiну повинен бути бiльшим за нуль!")
    
#     euro_amount = usd_amount * exchange_rate
#     print(f"Сума в євро: {euro_amount}")

# except ValueError:
#     print("Введiть коректне число")
# except Exception as e:
#     print(f"Помилка: {e}")
# finally:
#     print('Операцiя завершена')

# Задание 3

# try:
#     input_grades = input("Введiть оцiнки студентiв через пробiл: ").split()
#     grades = [float(grade) for grade in input_grades]

#     average_grade = sum(grades) / len(grades)
#     print(f"Середня оцінка студентів: {average_grade}")

# except ValueError:
#     print("Введiть коректні числа")
# except ZeroDivisionError:
#     print("Неможливо обчислити середню оцінку порожнього списку")
# finally:
#     print('Завершення обчислень')

# Задание 4

# input_balance = int(input("Введiть баланс рахунку: "))
# balance = input_balance

# try:
#     amount_str = int(input(f"Ваш баланс: {balance} введiть суму для зняття кратну 10: "))
#     amount = amount_str

#     if amount <= 0:
#         raise Exception('Некоректна сума для зняття')
#     if amount % 10 != 0:
#         raise ValueError('Сума повина бути кратна 10')
    

#     balance -= amount
#     print(f'Ви зняли {amount}, залишилось {balance} долларiв')

# except ValueError:
#     print('Сума повина бути кратна 10')
# except Exception as e:
#     print(e)

# finally:
#     print('Транзакцiю завершено')

# Задание 5

# order_num = input("Введiть номер замовлення (наприклад ORD001): ")

# try:
#      if not order_num.startswith("ORD"):
#           raise Exception("Неправильний формат номера замовлення")
     
#      number_part = order_num[3:]

#      if not number_part.isdigit():
#          raise Exception("Неправильний формат номера замовлення")
     
#      print(f"Номер замовлення {order_num} коректний")

# except Exception as e:
#     print(e)

# finally:
#     print("Перевірка завершена")

# Задание 6

# user_input = input("Введіть числа через пробіл: ")

# try:
#     elements = user_input.split()
#     numbers = []

#     for item in elements:
#         try:
#             num = float(item)
#             numbers.append(num)
#         except ValueError:
#             print(f"'{item}' буде пропущено")

#     try:
#         total = sum(numbers)
#         average = total / len(numbers)

#         print(f"cума: {total}")
#         print(f"cереднє значення: {average}")

#     except ZeroDivisionError:
#         print("немає коректних чисел для обчислення")

# finally:
#     print("обробку завершено")