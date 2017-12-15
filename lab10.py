def cmmdc(a, b):
    if x % y:
        return y

    return cmmdc(y, x % y)


def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


print(binary_search([3, 4, 5, 6, 12], 6))
print(binary_search([13, 16, 20, 2, 3], 4))


def permutation(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []

    for i in range(len(lst)):
        m = lst[i]

        remLst = lst[:i] + lst[i + 1:]

        for p in permutation(remLst):
            l.append([m] + p)
    return l


data = list('123')
for p in permutation(data):
    print p


def power(x, n):
    if n == 1:
        return x
    elif n == 2:
        return x * x
    else:
        aux = power(x, n/2)

        if n % 2 == 1:
            return x * aux * aux
        else:
            return aux * aux


print power(2, 3)