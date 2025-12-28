num1 = float(input("Введiть перше число: "))
num2 = float(input("Введiть друге число: ")) 
num3 = float(input("Введiть третє число: "))
chose_operation = input("Виберiть дiю + або *:  ")

if chose_operation == "+":
    print(f"{num1} + {num2} + {num3} = {num1 + num2 + num3}")
elif chose_operation == "*":
    print(f"{num1} * {num2} * {num3} = {num1 * num2 * num3}")