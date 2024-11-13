PRICE_PER_SQUARE_METER = 7.61
DISCOUNT = 0.18

greening_area = float(input())

sum_total = greening_area * PRICE_PER_SQUARE_METER
discount_price =  sum_total * DISCOUNT
sum_total_w_disc = sum_total - discount_price

print(f"The final price is: {sum_total_w_disc} lv.")
print(f"The discount is: {discount_price} lv.")
