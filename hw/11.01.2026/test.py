dollar = float(input("dollar = "))
curs = float(input("curs = "))
money = input("money(Eur, Gbp, Uah)  = ")
if money == "Eur":
    print(dollar * curs)
elif money == "Gbp":
    print(dollar * curs)
elif money == "Uah":
    print(dollar * curs)
else:
    print("error")