salary = float(input("Введіть вашу зп: ")) 
credit = float(input("Введіть суму яку треба внести по кредиту: "))
bills = float(input("Введіть суму борга по комуналці: "))

print(f"Після всіх виплат залишиться {salary - credit - bills} гривень")