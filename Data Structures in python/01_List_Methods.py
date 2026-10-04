nums=[10,20,30,40]

#origenal list
print(nums)
#After append 50 in nums
nums.append(50)      #add iteam or element at last of a list
# nums.append([60,70])     #this [60,70] is considered as one element here it shows an error but it was fine
print(nums)

#Extend method
num=[80,90]
nums.extend(num)        #Writed any iteratiable at last of original list
print(nums)

#insert method
#format list.insert(index, item)
nums.insert(1,15)
print(nums)

#4th
#remove() deletes the first matching value from the list.
nums.remove(10)
print("10 was removed:",nums)

n=[10,20,30,40,50]
#5th
#pop :pop() removes an element using its index and returns that removed element.
n1=n.pop(4)

print("After pop number at index 4 list is:",n)
print("and elemnet is :",n1)

print("*"*20)

#6th
#clear() removes all elements from list
nums.clear()
print("After clear function on nums list is: ",nums)

print("*"*20)

#7th
#index() tells you the position of a value.
print("Index of 30 in list n is :",n.index(30))

#8th
#count() tells you how many times a value occurs.
print("Count of 10 in list n is:",n.count(10))

l=[10,10,20,30,10]

print("Count of 10 occurs in l list",l.count(10))

print("*"*20)

#9th
#copy() creates a separate copy of a list
new_copy=n.copy()
print("Copy list of n is:",new_copy)

print("*"*20)

#10th
#reverse() reverses the current order of the list.
print("After reverse list n is:",n.reverse())

#11th
#sort() arranges the list in ascending order by default.
numbers = [50, 10, 40, 20, 30]
numbers.sort()
print(numbers)