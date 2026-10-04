s1={12,13,14,15,16}

#add() method aadd element in the set rendom place
s1.add(17)
print("After adding element 17 in set,the set is:",s1)

#remove() method removes element from set
s1.remove(12)
print("After remove 12 from set, the set will be:",s1)

#discard() methos ,if the element was present in set then it will de reomved or else it don't give an error
# s1.remove(1212) gives an error
s1.discard(1212) 

#pop() method will remove an random element form the set
s1.pop()
print("After pop random element from the set,the set will be:",s1)
