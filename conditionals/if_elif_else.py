#to check eligible for voting
age=int(input("Enter age: "))

if age>=18:
    print("Congrats ! You are eligible for vote.")

elif age<0:
    print("Invalid input!...")

else:
    print("you are not eligible for voting.")


