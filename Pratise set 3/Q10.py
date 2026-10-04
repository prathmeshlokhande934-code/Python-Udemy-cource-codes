# Write a program that takes a list of numbers and removes all duplicates using a set
my_list=[]
n=int(input("Enter how amny ele wnat to add in list:"))

for i in range(0,n):
    num=int(input("Enter the number:"))
    my_list.append(num)

my_set=set(my_list)
print(my_set)
