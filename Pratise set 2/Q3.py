# Write a program that takes a number from the user and prints “Even” if it is even, otherwise “Odd”.

num=int(input("Enter any number: "))

if num%2==0:
    print("Number is even.")

elif num%2!=0:
    print("Number is odd.")

else:
    print("Invalid input")