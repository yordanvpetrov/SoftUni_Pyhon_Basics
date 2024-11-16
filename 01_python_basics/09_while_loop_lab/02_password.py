user_name = input()
password = input()

input_password = ""

while input_password != password:
    input_password = input()

    if input_password == password:
        print(f"Welcome {user_name} !")
        break