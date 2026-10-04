#Write a program that counts how many vowels are in a given string

text="My name is Prathmesh and my surname is A Lokhande What is yours ?"
text=text.lower()
vowels=["a","e","i",'o','u']
count=0

for char in text:
    if char in vowels:
        count+=1

    else:
        continue
print(f"Ther are {count} vowels in given string")