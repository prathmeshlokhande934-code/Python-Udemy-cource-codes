#printing an number in fibonacci series of index usig recurrsion
'''
Fibonacci series :
series  =  0 1 1 2 3 5 8 13 21 34 ........AND SO ON
index   =  0 1 2 3 4 5 6  7  8  9 ........AND SO ON
formula for fibonacci series using reccurssion: 
fib(n-2)+fib(n-1)
'''

def fib(n):
    if (n==0 or n==1):
        return n
    return fib(n-2)+fib(n-1)

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))