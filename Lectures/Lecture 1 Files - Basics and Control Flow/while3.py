number_of_loops = int(input("How many loops to perform? "))
loops_completed = 0

while loops_completed < number_of_loops:
    print("Finite loop")
    if loops_completed == 3:
        print("That was the fourth loop")
    loops_completed = loops_completed + 1
