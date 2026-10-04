# Print the multiplication table of a number (entered by user).

num=int(input("Enter any number: "))

for i in range(1,11):
    print(f"{i} x {num} = {num*i}")
