
def sum_of_digits(n):
    if n==0:
        return 0
    sum=0
    for i in range(1,n+1):
        digit=n%10
        sum=sum+digit
        n=n//10
    return sum    

print(sum_of_digits(222))


