#Write a program using match case that simulates a simple calculator. Ask the user for two numbers and an operation (+, -, *, /). Perform the operation using match case .


print("1.Addition.\n2.Substraction.\n3.Multiplication.\n4.Division.")
while True:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))

    choice=int(input("Enter the choice: "))

    match choice:
        case 1:
            result=num1+num2
        case 2:
            result=num1-num2
        case 3:
            result=num1*num2
        case 4:
            result=num1/num2
        case _:
            print("Invalid input.")
            break
    print(result)

