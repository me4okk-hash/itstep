money = float(input("Введіть загальну суму рахунку: "))
people = int(input("Введіть кількість осіб: "))
tips = money * 0.15
total = money + tips
per_person = total / people

print(f"Сума чайових 15%: {tips}")
print(f"Загальна сума з чайовими: {total}")
print(f"Кожна людина має заплатити: {per_person}")