PEN_PRICE = 5.80
MARKER_PRICE = 7.20
CLEANING_AGENT_PRICE = 1.20

pens = int(input())
markers = int(input())
cleaning_agent = int(input())
discount_percent = int(input())

discount = discount_percent / 100

sum_total = (pens * PEN_PRICE) + (markers * MARKER_PRICE) + (cleaning_agent * CLEANING_AGENT_PRICE)

sum_w_disc = sum_total - sum_total * discount
print(sum_w_disc)
