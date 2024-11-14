PUZZLE_PRICE = 2.60
DOLL_PRICE = 3
PLUSH_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2
THRESHOLD_DISCOUNT = 0.25
RENT_PERCENT = 0.10

vacation_price = float(input())
puzzles = int(input())
dolls = int(input())
plush_bears = int(input())
minions = int(input())
trucks = int(input())

sum_toys = puzzles + dolls + plush_bears + minions + trucks
sum_profit = ((puzzles * PUZZLE_PRICE)
              + (dolls * DOLL_PRICE)
              + (plush_bears * PLUSH_BEAR_PRICE)
              + (minions * MINION_PRICE)
              + (trucks * TRUCK_PRICE))


if sum_toys >= 50:
    sum_profit = sum_profit - sum_profit * THRESHOLD_DISCOUNT

final_profit = sum_profit - sum_profit * RENT_PERCENT

if final_profit >= vacation_price:
    print(f"Yes! {final_profit - vacation_price:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price - final_profit:.2f} lv needed.")
