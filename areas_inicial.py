def calc(t, a, b=0):
    if t == 1:
        return 3.1416 * a * a
    elif t == 2:
        return a * b
    elif t == 3:
        return (a * b) / 2
    else:
        return 0


print("Area:", calc(1, 5))
print("Area:", calc(2, 4, 6))
print("Area:", calc(3, 4, 6))
