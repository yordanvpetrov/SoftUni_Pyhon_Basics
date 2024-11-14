DECOR_PERCENT = 0.10
THRESHOLD_DISCOUNT = 0.10

budget = float(input())
statists = int(input())
clothes_price = float(input())

if statists >= 150:
    clothes_price = clothes_price - clothes_price * THRESHOLD_DISCOUNT

decor_price = budget * DECOR_PERCENT
clothes_cost = statists * clothes_price

sum_total = decor_price + clothes_cost

if sum_total > budget:
    total = sum_total - budget
    print("Not enough money!")
    print(f"Wingard needs {total:.2f} leva more.")
else:
    total = budget - sum_total
    print("Action!")
    print(f"Wingard starts filming with {total:.2f} leva left.")
