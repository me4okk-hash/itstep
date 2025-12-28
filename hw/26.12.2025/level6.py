car_rent = float(input("Введіть вартість аренди автомобіля за день: "))
days_rent = int(input("Введіть кількість днів аренди: "))
deposit_amount = float(input("Введіть суму застави: "))
rent = car_rent * days_rent
total_initial = rent + deposit_amount
amount_after_return = rent
days_rent = days_rent + (days_rent == 0)
cost_per_day = rent / days_rent

print(f"Сума яку потрібно внести при отриманні автомобіля: {total_initial}")
print(f"Вартість аренди після повернення застава повертається: {amount_after_return}")
print(f"Сума застави яка повертається: {deposit_amount} ")
print(f"Вартість аренди за 1 день: {cost_per_day} ")