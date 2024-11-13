movie_name = input()
days_qty = int(input())
tickets_qty = int(input())
ticket_price = float(input())
cinema_tax = int(input()) / 100

profit = (days_qty * tickets_qty) * ticket_price

profit -= profit * cinema_tax

print(f"The profit from the movie {movie_name} is {profit:.2f} lv.")
