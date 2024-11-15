ROSE_PRICE = 5
DAHLIA_PRICE = 3.80
TULIP_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

ROSE_THRESHOLD = 0.10
DAHLIA_THRESHOLD = 0.15
TULIP_THRESHOLD = 0.15
NARCISSUS_THRESHOLD = 0.15
GLADIOLUS_THRESHOLD = 0.20

flower_type = input()
flower_quantity = int(input())
budget = int(input())

sum_total = 0

if flower_type == "Roses":
    sum_total = flower_quantity * ROSE_PRICE
    if flower_quantity > 80:
        sum_total -= (sum_total * ROSE_THRESHOLD)
elif flower_type == "Dahlias":
    sum_total = flower_quantity * DAHLIA_PRICE
    if flower_quantity > 90:
        sum_total -= (sum_total * DAHLIA_THRESHOLD)
elif flower_type == "Tulips":
    sum_total = flower_quantity * TULIP_PRICE
    if flower_quantity > 80:
        sum_total -= (sum_total * TULIP_THRESHOLD)
elif flower_type == "Narcissus":
    sum_total = flower_quantity * NARCISSUS_PRICE
    if flower_quantity < 120:
        sum_total += (sum_total * NARCISSUS_THRESHOLD)
elif flower_type == "Gladiolus":
    sum_total = flower_quantity * GLADIOLUS_PRICE
    if flower_quantity < 80:
        sum_total += (sum_total * GLADIOLUS_THRESHOLD)

money = abs(budget - sum_total)

if sum_total <= budget:
    print(f"Hey, you have a great garden with {flower_quantity} {flower_type} and {money:.2f} leva left.")
else:
    print(f"Not enough money, you need {money:.2f} leva more.")
