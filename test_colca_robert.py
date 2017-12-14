def alg(n):
    i = 0
    s = n % 10
    n /= 10

    while n > 0:
        i += 1
        s += n % 10
        n /= 10

    return s


def count_descending_elements(x):
    cate = 1

    for i in range(0, len(x)-1):
        if x[i] <= x[i+1]:
            return cate

        cate += 1


number = input("Numar: ")

print "Suma cifrelor: ", alg(number)

print "[7, 3, 1, 4]: ", count_descending_elements([7, 3, 1, 4])
print "[1, 7, 3, 5]: ", count_descending_elements([1, 7, 3, 5])
print "[1, 2, 3]: ", count_descending_elements([1, 2, 3])
