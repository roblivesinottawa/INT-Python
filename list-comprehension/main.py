# the squares of the first ten natural numbers
nums = []

for n in range(1, 11):
    nums.append(n ** 2)

print(nums)

# with list comp
nums_ = [x**2 for x in range(1, 11)]
print(nums_)