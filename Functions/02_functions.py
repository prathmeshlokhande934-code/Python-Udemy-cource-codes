#there are three types of arguments given in the function
#1st is positional arguments

def addition(a,b):
    sum=a+b
    print(sum)

addition(1,2) #this is an example of positional arguments

print("_"*20)

#2nd is default arguments

def add2(a,b,c=0):  #here i set an default argument ,rember that default values are givenafter at last of all arguments if value of default argument was not given in function call the it uses its default value here it is 0

    print(a+b+c)

add2(2,3)
add2(2,3,1) #gere i gien the value to 'c' so this value will assine to 'c' changing its default value

print("_"*20)
#3rd is keyword argument

def add(a,b):
    sum=a+b
    print(sum)

add(b=2,a=3) #this is keyword arguments we can pass any value first using there keywoeds

