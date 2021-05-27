# find the product of a list using reduce
from functools import reduce
_list = [1,2,3,4,5,6,7,8,9,10]

product = reduce((lambda x, y : x * y), _list)
print(product)

greatest = reduce((lambda x, y: y if(y>x) else x), _list)
print(greatest)

smallest = reduce((lambda x, y: y if(y<x) else x), _list)
print(smallest)