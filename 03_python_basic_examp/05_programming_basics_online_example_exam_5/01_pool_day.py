from math import ceil

people_qty = int(input())
entre_tax = float(input())
lounge_price = float(input())
umbrela_price = float(input())

money_for_umbrellas = ceil((people_qty / 2)) * umbrela_price
money_for_lounges = ceil((people_qty * 0.75)) * lounge_price
money_for_tickets = people_qty * entre_tax

sum_total = money_for_umbrellas + money_for_lounges + money_for_tickets

print(f"{sum_total:.2f} lv.")
