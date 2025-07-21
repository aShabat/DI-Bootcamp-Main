# Write code that asks the user for a number and determines whether this number is odd or even.

n = int(input("Write a number: "))
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")
