kilometers = float(input("Введіть відстань у кілометрах: "))
fuel = float(input("Введіть витрату бензину на 100 кілометрів: "))
liter_costs = float(input("Введіть ціну за літр бензину: "))
total_fuel = kilometers / 100 * fuel
trip_cost = total_fuel * liter_costs

print(f"Загальна вартість поїздки: {trip_cost}")