# a built-in tool that applies a specified function to every item in an iterable (like a list, tuple, or dictionary) and returns an iterator containing the transformed results

#1st way to write map function
def square(x):
    return x**2
l1=[2,3,4]
print(list(map(square,l1)))


# print(list(map(square,l1)))

print("_"*20)

#2nd way
def add(x,y):
    return x-y

list1=[12,13,14] 
list2=[2,3,4]
print(list(map(add,list1,list2)))

print("_"*20)

#3rd way using lambda function

my_list1=[10,20,30]
my_list2=[1,2,3]
print(list(map(lambda x,y:x+y,my_list1,my_list2)))



