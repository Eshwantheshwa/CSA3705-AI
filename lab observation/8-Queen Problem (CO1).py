
def solve(row, queens):
    if row == 8:
        for q in queens:
            print("." * q + "Q" + "." * (7-q))
        return True

    for col in range(8):
        if all(col != c and abs(col-c) != row-r
               for r, c in enumerate(queens)):
            if solve(row + 1, queens + [col]):
                return True
    return False

solve(0, [])
