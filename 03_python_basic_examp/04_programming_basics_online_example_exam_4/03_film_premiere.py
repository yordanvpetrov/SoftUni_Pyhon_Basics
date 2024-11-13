JW_DRINK_PRICE = 12
JW_POPCORN_PRICE = 15
JW_MENU_PRICE = 19

SW_DRINK_PRICE = 18
SW_POPCORN_PRICE = 25
SW_MENU_PRICE = 30

JUMANJI_DRINK_PRICE = 9
JUMANJI_POPCORN_PRICE = 11
JUMANJI_MENU_PRICE = 14

SW_FOUR_TICKETS_DISCOUNT = 0.30 # applies for 4 tickets or over
JUMANJI_TICKETS_DISCOUNT = 0.15 # applies for only 2 tickets

movie_name = input()
ticket_type = input()
tickets_qty = int(input())

price = 0

if movie_name == "John Wick":
    if ticket_type == "Drink":
        price = tickets_qty * JW_DRINK_PRICE
    elif ticket_type == "Popcorn":
        price = tickets_qty * JW_POPCORN_PRICE
    elif ticket_type == "Menu":
        price = tickets_qty * JW_MENU_PRICE
elif movie_name == "Star Wars":
    if ticket_type == "Drink":
        price = tickets_qty * SW_DRINK_PRICE
    elif ticket_type == "Popcorn":
        price = tickets_qty * SW_POPCORN_PRICE
    elif ticket_type == "Menu":
        price = tickets_qty * SW_MENU_PRICE
elif movie_name == "Jumanji":
    if ticket_type == "Drink":
        price = tickets_qty * JUMANJI_DRINK_PRICE
    elif ticket_type == "Popcorn":
        price = tickets_qty * JUMANJI_POPCORN_PRICE
    elif ticket_type == "Menu":
        price = tickets_qty * JUMANJI_MENU_PRICE

if tickets_qty >= 4 and movie_name == "Star Wars":
    price -= price * SW_FOUR_TICKETS_DISCOUNT
elif tickets_qty == 2 and movie_name == "Jumanji":
    price -= price * JUMANJI_TICKETS_DISCOUNT

print(f"Your bill is {price:.2f} leva.")
