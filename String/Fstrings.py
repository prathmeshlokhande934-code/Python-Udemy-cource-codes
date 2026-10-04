#String formating

template="Hy {} you are ausome,take this {}$."

a="Prathmesh"
a2=10000

b="Omkar"
b2=100

c="Vedant"
c2=1000

t1=template.format(a,a2)  #Befor the fstring exist this gow the varialble values are inseted in a string using format function
t2=template.format(b,b2)
t3=template.format(c,c2)

print(t1)
print(t2)
print(t3)

#But after fstring was come we write like this
print("_"*20)

print(f"Hy {a} take this {a2}$")
print(f"Hy {b} take this {b2}$")
print(f"Hy {c} take this {c2}$")