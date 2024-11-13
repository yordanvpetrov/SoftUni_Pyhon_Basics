DUBAI_WINTER = 45_000
DUBAI_SUMMER = 40_000

SOFIA_WINTER = 17_000
SOFIA_SUMMER = 12_500

LONDON_WINTER = 24_000
LONDON_SUMMER = 20_250

DUBAI_DISCOUNT = 0.3
SOFIA_EXTRA = 0.25

budget = float(input())
destination = input()
season = input()
days = int(input())

movie_cost = 0

if season == "Summer":
    if destination == "Dubai":
        movie_cost = DUBAI_SUMMER
        movie_cost -= movie_cost * DUBAI_DISCOUNT
    elif destination == "Sofia":
        movie_cost = SOFIA_SUMMER
        movie_cost += movie_cost * SOFIA_EXTRA
    elif destination == "London":
        movie_cost = LONDON_SUMMER
elif season == "Winter":
    if destination == "Dubai":
        movie_cost = DUBAI_WINTER
        movie_cost -= movie_cost * DUBAI_DISCOUNT
    elif destination == "Sofia":
        movie_cost = SOFIA_WINTER
        movie_cost += movie_cost * SOFIA_EXTRA
    elif destination == "London":
        movie_cost = LONDON_WINTER

sum_total = movie_cost * days

if budget >= sum_total:
    print(f"The budget for the movie is enough! We have {budget - sum_total:.2f} leva left!")
else:
    print(f"The director needs {sum_total - budget:.2f} leva more!")
