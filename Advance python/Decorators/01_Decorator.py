# Decorator is a function,which takes a function as an argument,                                                                         
def decorator(func):                #declaring the decorator,and passing the function using func variable,Here the func=add happens.

    def weapper():                  #wrapping occurs

        print("process is started") #want to run before main process code

        func()                      #main process or function

        print("Process is ended.")  #process after the main process

    return weapper                  #returning the wrpper function ,dont give the brackests if it was given then it will call the wrapper function insted or returning it

#main function that wnat to exciute
def add():
    n1=int(input("Enter any number:"))
    n2=int(input("Enter any number:"))
    print(n1+n2)

n=decorator(add)                    #calling the decorator for the main function thant want to execute,here also dont give the brackets for same reason above mensioned and storing it in to n varible

n()             #now here now we call the function was returned to n ,her we wnant to give brackets
     