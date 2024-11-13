budget = float(input())
nights = int(input())
night_price = float(input())
percent_extra_expenses = int(input()) / 100

if nights > 7:
    night_price -= night_price * 0.05

expenses = budget * percent_extra_expenses

total_price = nights * night_price + expenses
    
if budget >= total_price:
    print(f"Ivanovi will be left with {budget - total_price:.2f} leva after vacation.")
else:
    print(f"{total_price - budget:.2f} leva needed.")
