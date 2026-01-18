# Задание 1 
# exam_score = int(input('введите оценку (0-100): '))

# if exam_score < 100 and exam_score > 90:
#     print('Відмінно')
# elif exam_score < 89 and exam_score > 70:
#     print('Добре')
# elif exam_score < 69 and exam_score > 50:
#     print('Задовільно')
# elif exam_score < 50:
#     print('Незадовільно')

# Задание 2
# salary = int(input('Ваша зарплата: '))
# years_works = float(input('Введите число лет которое вы работаете в фирме: '))
# award = salary / 100

# if years_works > 5:
#     print((award*15)+salary)
# elif years_works < 5 and years_works > 3:
#     print((award*10)+salary)
# elif years_works < 3 and years_works > 1:
#     print((award*5)+salary)
# elif years_works < 1:
#     print('Премія не передбачена')

# Задание 3

# numbers = int(input('Введiть цiле чотирчисло: '))
# num1 = numbers % 10
# num2 = (numbers % 100 - numbers % 10) / 10
# num3 = (numbers % 1000 - numbers % 100) / 100
# num4 = (numbers - (num1 + (num2 * 10)+(num3 * 100))) / 1000
# if (num1 + num2 + num3 + num4) % 2 == 0:
#     print('Сума цифр парна')
# else:
#     print('Сума цифр непарна')

# Задание 4
# numbers = int(input("Введiть шестизначне число: "))

# a1 = numbers // 100000
# b1 = (numbers // 10000) % 10
# c1 = (numbers // 1000) % 10
# d1 = (numbers // 100) % 10
# e1 = (numbers // 10) % 10
# f1 = numbers % 10
# if numbers >= 100000 and numbers <= 999999:
#     if (a1 + b1 + c1) == (d1 + e1 + f1):
#         print("Число є щасливим")
#     else:
#         print("Число не є щасливим")
# else:
#     print("Введено не шестизначне число")

# Задание 5

# numbers = int(input("Введiть шестизначне число: "))

# a1 = numbers // 100000
# b1 = (numbers // 10000) % 10
# c1 = (numbers // 1000) % 10
# d1 = (numbers // 100) % 10
# e1 = (numbers // 10) % 10
# f1 = numbers % 10

# if 100000 <= numbers <= 999999:
#     new_num = f1 * 100000 + e1 * 10000 + c1 * 1000 + d1 * 100 + b1 * 10 + a1
#     print(int(new_num))
# else:
#     print("Введено не шестизначне число")