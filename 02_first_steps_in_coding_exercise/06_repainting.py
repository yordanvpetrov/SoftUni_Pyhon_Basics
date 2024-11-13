NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5.00
BAG_PRICE = 0.40
WORKERS_PRICE = 0.30

nylon = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())

paint_total = (paint + paint * 0.10) * PAINT_PRICE
nylon_total = (nylon + 2) * NYLON_PRICE
thinner_total = thinner * THINNER_PRICE

materials_total = paint_total + nylon_total + thinner_total + BAG_PRICE
work_price = (materials_total * WORKERS_PRICE) * work_hours

sum_total = materials_total + work_price
print(sum_total)