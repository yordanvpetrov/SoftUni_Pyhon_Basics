deposit = float(input())
term_deposit = int(input()) / 100
annual_interest_rate = float(input())

total = deposit + term_deposit * ((deposit * annual_interest_rate) / 12)
print(total)
