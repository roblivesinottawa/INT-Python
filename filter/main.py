another_list = [1, 2, 3, 4, 5, 6]

odds = list(filter((lambda x: x % 2 != 0), another_list))
print(odds)

evens = list(filter((lambda y : y % 2 == 0), another_list))
print(evens)