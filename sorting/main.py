from operator import itemgetter

record = [ 
        {'name': 'Rob', 'score': 10, 'age': 34}, 
        {'name': 'Vick', 'score':9, 'age': 30}, 
        {'name': 'Sam', 'score': 9.5, 'age': 30}, 
        {'name': 'John', 'score': 8, 'age': 27}
        ]

sorted_results = sorted(record, key=itemgetter('score', 'age'))
print(sorted_results)