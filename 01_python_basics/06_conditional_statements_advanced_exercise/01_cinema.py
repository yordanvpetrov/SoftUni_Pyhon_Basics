PREMIERE_TICKET = 12.00
NORMAL_TICKET = 7.50
DISCOUNT = 5.00

movie_type = input()
rows = int(input())
columns = int(input())

tickets_qty = rows * columns

income = 0

if movie_type == "Premiere":
    income = tickets_qty * PREMIERE_TICKET
elif movie_type == "Normal":
    income = tickets_qty * NORMAL_TICKET
elif movie_type == "Discount":
    income = tickets_qty * DISCOUNT

print(f"{income:.2f} leva")
