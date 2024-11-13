annual_tax = int(input())

shoes = annual_tax - annual_tax * 0.40
team = shoes - shoes * 0.20
ball = team / 4
accessories = ball / 5

sum_total = annual_tax + shoes + team + ball + accessories
print(sum_total)
