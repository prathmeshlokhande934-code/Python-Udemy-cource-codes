#global key word was used when we want to chagenge the global variable inside the function.

def sum(a,b):
    global z    #use of global key word
    z=10        #updated z value
    sum=a+b
    return sum

z=0     #global variable 
print(sum(2,3))
print(z)
