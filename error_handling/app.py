a = int(input("Enter an integer: >>> "))

if a == 0:
    raise ZeroDivisionError("Cannot divide by zero!")
print(a)