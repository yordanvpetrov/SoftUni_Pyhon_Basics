balance = 0

while True:
    command = input()

    if command == "NoMoreMoney":
        print(f"Total: {balance:.2f}")
        break

    command = float(command)

    if command < 0:
        print(f"Invalid operation!")
        print(f"Total: {balance:.2f}")
        break
    else:
        balance += float(command)
        print(f"Increase: {float(command):.2f}")
