def log_call(func):
    def wrapper():
        print("Calling greet!....")
        func()
        print("greet finished!...")

    return wrapper

@log_call
def greet():
    print("Hello Prathmesh")

greet()