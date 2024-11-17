start = input()
stop = input()

for num_one in range(int(start[0]), int(stop[0]) + 1):
    for num_two in range(int(start[1]), int(stop[1]) + 1):
        for num_three in range(int(start[2]), int(stop[2]) + 1):
            for num_four in range(int(start[3]), int(stop[3]) + 1):
                if num_one % 2 != 0 and num_two % 2!= 0 and num_three % 2 != 0 and num_four % 2 !=0:
                    print(f"{num_one}{num_two}{num_three}{num_four}", end=" ")
