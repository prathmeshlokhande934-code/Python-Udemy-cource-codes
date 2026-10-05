def decorator(func):
    def wrapper():
        print("Process stated")
        func()
        print("Process end")

    return wrapper

@decorator      #here this is how wew can use decorator without writting this code "n=decorator(add) and n()".
def add():
    n1=int(input("Enter 1st num:"))
    n2=int(input("Enter 2nd num:"))
    print(n1+n2)

add()

