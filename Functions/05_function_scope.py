x=10    #this x is global variable

def num():
    x=5     #this x is local variable
    return f"Local variable inside the function: {x}"

print(num())
print("Global variable outside the function:",x)

#Local variable: Mens a variable declared inside the function only is called local variable. also when function return something or function was executed the local variables are removed from memory.

#global variable: Mena variable declared outside the function is callled global variable,Global variaible was not redifined in function insted it acts live an indivisual local variable.