def remove_duplicates(a):
    print list(set(a))


remove_duplicates([1, 2, 2, 3, 4, 5, 5, 5, 7, 9])


def is_in_list(x, a):
    for el in a:
        if x == el:
            return 1

    return 0


def intersect_lists(a, b):
    intersection_list = []

    for i in range(len(a)):
        if is_in_list(a[i], b):
            intersection_list.append(a[i])

    return intersection_list


print "Intersectia: ", intersect_lists([1, 2, 6, 4, 5, 3], [2, 3, 4, 1])

