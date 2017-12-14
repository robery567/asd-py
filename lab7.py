from Classes.sorting import Sorting

sorting_list = [4, 3, 2, -7, - 10]
sorter = Sorting(sorting_list)

sorter.insert()

print "Insert sort: "
print "Lista: ", sorting_list
print "Lista sortata: ", sorter.get_list()
print "Numar comparatii: ", sorter.get_comparations_count()
print "Numar mutari: ", sorter.get_moves_count()

sorting_list2 = [4, 3, 2, -7, - 10]
sorter2 = Sorting(sorting_list2)

sorter2.bubble()

print "Bubble sort: "
print "Lista: ", sorting_list2
print "Lista sortata: ", sorter2.get_list()
print "Numar comparatii: ", sorter2.get_comparations_count()
print "Numar mutari: ", sorter2.get_moves_count()

sorting_list3 = [4, 3, 2, -7, - 10]
sorter3 = Sorting(sorting_list3)

sorter3.selection()

print "Selection sort: "
print "Lista: ", sorting_list3
print "Lista sortata: ", sorter3.get_list()
print "Numar comparatii: ", sorter3.get_comparations_count()
print "Numar mutari: ", sorter3.get_moves_count()
