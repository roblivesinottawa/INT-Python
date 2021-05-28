# args
def add(*nums):
    return sum(nums) 

print(add(10, 20, 30, 40))

# kwargs
def information(**data):
    return data

print(information(name='Rob', age=34, occupation='programmer'))


def get_data(search_engine, *queries, **props):
    return search_engine, queries, props

print(get_data('google', 'learn JavaScript', 'Python', 'Flask', limit=100))