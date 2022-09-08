# This code takes a positive integer(n) and outputs the first n fibonacci sequence starting from 0

num = int(input("Enter a number to generate fibonacci sequence: "))


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(num):
    print(fibonacci(n))
