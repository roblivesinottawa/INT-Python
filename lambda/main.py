# lambdas are unnnamed functions
power = lambda a, b : a**b
print(power(10, 10))


# another way would be with a traditional function:
def power(a, b):
    return a ** b


list_ = [1,2,3,4,5]
average_ = lambda L : sum(L) / len(L)
print(average_(list_))