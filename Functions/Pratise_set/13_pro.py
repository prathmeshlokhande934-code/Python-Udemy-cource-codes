# Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers

def fibonacci(n):

    def fib(k):
        if k==0 or k==1:
            return k
        return fib(k-2)+fib(k-1)

    for i in range(n):
        print(fib(i),end=" ")
        
fibonacci(10)

