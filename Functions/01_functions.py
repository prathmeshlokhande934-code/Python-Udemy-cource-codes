# a=int(input("Enter any number: "))
# b=int(input("Enter any number: "))
# c=int(input("Enter any number: "))

# avgerage=(a+b+c)/3
# print(avgerage)

# def average():
#     a=int(input("Enter any value:"))
#     b=int(input("Enter any value:"))
#     c=int(input("Enter any value:"))

#     avg=(a+b+c)/3
#     print(avg)

# average()

#or

def avge(a,b,c):
    avg=(a+b+c)/3
    print(avg)

avge(1,2,3)

#or using return 

def avg(a,b,c):
    avg=(a+b+c)/3
    return avg      #here this "return" will give avg value to return back to function to assine other variable

result=avg(1,2,3)
print(result)


