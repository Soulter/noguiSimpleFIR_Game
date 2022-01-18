def print_chess(chess):
    count = 0
    for i in chess:
        if i == 0:
            print("-   ", end="")
            count += 1
        if i == 1:
            print("O   ", end="")
            count += 1
        if i == 2:
            print("X   ", end="")
            count += 1
        if count % 3 == 0:
            print("\n", end="")
