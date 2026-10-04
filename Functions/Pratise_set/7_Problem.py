def factorial(n):
    if n==0 or n==1:
        return n

    return n*factorial(n-1)

num=int(input("ENTER ANY NUMBER: "))
print(factorial(num))

# A factorial is the product of a whole number and all the whole numbers below it,
# Common Examples
# (1!) = (1)
# (3!) = (3 times 2 times 1 = 6)
# (4!) = (4 times 3 times 2 times 1 = 24)
# (5!) = (5 times 4 times 3 times 2 times 1 = 120)
