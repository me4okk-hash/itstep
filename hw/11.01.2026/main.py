'''
print("Hello, World!")
print(10)
print(10, 12, 14)
print(10, 5,6,6 ,sep=',')

# Тип даних - харакетеристика даних, яка визначає діапазон значень та набір доступних операцій.

#srt - послідовність символів
#int - цілі числа
#float - дробові числа

print(type(10 / 4))

# Змінна - іменована область пам'яті, що зберігає значення певного типу і може його змінювати
# протягом виконання програми.

group = 'П511'
print(type(group))
group = 511
print(type(group))

weather = input("Введіть поточну погоду: ")
print(weather)

number1 = float(input("Введіть число: "))
print(type(number1))
number2 = float(input("Введіть число: "))
print(f"{number1} ** {number2} = {number1 ** number2}")


# bool - True або False

can_penguins_swim = True
can_penguins_fly = False

print(f"Чи можуть пінгвіни літати? {can_penguins_fly}")
print(f"Чи можуть пінгвіни плавати? {can_penguins_swim}")
print(type(can_penguins_swim))
print(type(can_penguins_fly))


number = int(input("Введіть ціле число: "))

print(f"{number} > 10? {number > 10}")
print(f"{number} >= 10? {number >= 10}")
print(f"{number} < 10? {number < 10}")
print(f"{number} <= 10? {number <= 10}")
print(f"{number} == 10? {number == 10}")
print(f"{number} != 10? {number != 10}")
'''

# is_raining = input("Чи іде зараз дощ? (так/ні) ")

# if is_raining == 'так':
#     print("Беремо парасолю!")

# is_cold = input("Чи зараз холодно? (так/ні) ")

# if is_cold == 'так':
#     print("Вдягаємо теплий одяг")
# else:
#     print("Вдягаємо легкий одяг")
'''

temperature = int(input("Скільки зараз градусів на вулиці? "))

if temperature <= -10:
    print("Вдягаємось дуже тепло: рукавички, термобілизна, зимова шуба, зимові штанці, черевики")
elif temperature > -10 and temperature <= 5: # else if
    print("Вдягаємось тепло: куртка, теплі штанці, теплі кросівки")
elif temperature > 5 and temperature <= 16:
    print("Вдягаємось легко: кофта, сорочка, кеди, легкі штанці")
else:
    print("Вдягаємось по-літньому: футболка, шорти, шкльопки і на море!")



print("Виходимо на вулицю!")

# Оператори об'єднання - and, or - об'єднають результат двох логічних виразів.

print(f"True and True = {True and True}")
print(f"False and True = {False and True}")
print(f"True and False = {True and False}")
print(f"False and False = {False and False}")

print()

print(f"True or True = {True or True}")
print(f"False or True = {False or True}")
print(f"True or False = {True or False}")
print(f"False or False = {False or False}")

print()

# not - інвертує значення bool
print(f"not True = {not True}")
print(f"not False = {not False}") 


# number = int("10")

boolean = bool(0) # False

print(bool(0)) # False
print(bool(0.0)) # False
print(bool('')) # False

something = None
print(bool(something)) # 

print(bool(10)) # True
print(bool(-6.8)) # True
print(bool('hello')) # True
'''

#Калькулятор
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

operation = input("Оберіть операцію (+, -, *, /): ")

if operation == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == "/":
    if num2 == 0:
        print("Не можна ділити на нуль")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Некоректна операція!")