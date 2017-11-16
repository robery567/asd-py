def find_largest_number(x):
    if x % 3 == 0:
        state = 1
    else:
        state = 2

    while x > 0:
        a.append(state)
        x -= state
        state = 3 - state

a = []
find_largest_number(42)

print a[::-1]

print a