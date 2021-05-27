list_ = [3, 34, 56, 75, 98, 13, 45]

odds = [x for x in list_ if x%2 != 0]
print(list(reversed(odds)))

evens = [y for y in list_ if y % 2 == 0]
print(evens)