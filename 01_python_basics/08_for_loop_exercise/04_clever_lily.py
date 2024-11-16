age = int(input())
washer_price = float(input())
toys_price = int(input())

money = 0
toys_money = 0
brother_took = 0

for i in range(1, age +1):
    if i % 2 == 0:
        money += i * 5
        brother_took += 1
    else:
        toys_money += toys_price

sum_money = (money + toys_money) - brother_took

if sum_money >= washer_price:
    print(f"Yes! {sum_money - washer_price:.2f}")
else:
    print(f"No! {washer_price - sum_money:.2f}")
