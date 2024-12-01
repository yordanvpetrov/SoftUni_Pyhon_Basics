needed_money = float(input())
current_money = float(input())

spend_counter = 0
days_counter = 0
is_saved = True

while current_money < needed_money:
    action = input()
    money = float(input())
    days_counter += 1

    if action == "spend":
        spend_counter += 1
        current_money -= money
        if current_money <= 0:
            current_money = 0
        if spend_counter >= 5:
            is_saved = False
            break
    elif action == "save":
        spend_counter = 0
        current_money += money

if is_saved:
    print(f"You saved the money for {days_counter} days.")
else:
    print(f"You can't save the money.")
    print(f"{days_counter}")
