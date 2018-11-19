def print_move(fr, to):
    print("- Move top ring in '{}' tower to the '{}' tower".format(fr, to))

def Hanoi(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)

    else:
        Hanoi(n - 1, fr, spare, to)
        Hanoi(1, fr, to, spare)
        Hanoi(n - 1, spare, to, fr)

Hanoi(3, "A", "B", "C")
