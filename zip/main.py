# use zip function to connect 
name = ["John", "Rob", "Vick", "Sarah"]
age = [18, 19, 20, 21]
grade = ['A', 'C', 'A', 'B']

for info in zip(name, age, grade):
    print(info)


nums = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
for n in zip(*nums):
    print(n)