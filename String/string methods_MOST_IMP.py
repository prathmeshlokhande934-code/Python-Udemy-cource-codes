s1="hello my namen is prathmesh" #Important statement by using string methods we are not editing origernal string ,we are making new string using string methods. Mens string are immutable in python.

#1st method
a=len(s1)
print(a)
#2nd method
b=s1.upper()
print(b)
#3rd method
print(b.lower())
#4th method
print(b.capitalize())
#5th method
print(b.title())

print("*"*20)
#------------------------------------------
text="  hallow world  "
#6th method
print(text.strip()) #this function removes whitespace characters such as spaces, tabs (\t), and newlines (\n) and give neet string

#7th method 
print(text.lstrip()) #this function do this same thing but only at left side of string
#8th method
print(text.rstrip())#thi function will do in right side

print("*"*20)
#------------------------------------
#9th method
text="Python is an very very very ausome language"
print(text.find("is")) #this function will take argument of which word we want to find.,and it will write an first character index of the word.

#10th method
print(text.replace("very","so")) #this method will take two arguments ,first is the word which we want to replace and second is the word which replace.

print("*"*20)
#----------------------------------

#11th method
text="Python is very relible language for ML"
c=text.split(" ")
print(c)      #In Python, the split() method breaks a string into a list of substrings based on a specified delimiter. It is a built-in string method that scans a string from left to right, cuts it at matching points, and returns a new list without changing the original string. here i seprated from space to a list. And it also take an another argument which is maxsplit: The maximum number of splits to perform. The default value is -1, which means "all possible splits"

#12th method 
d=['Python', 'is', 'very', 'relible', 'language', 'for', 'ML']
print(" ".join(d))      #The join() method in Python is a built-in string method used to concatenate the elements of an iterable (such as a list, tuple, or set) into a single string, using a specified string as the separator basic syntax is "string_separator.join(iterable)"

#---------------------------------
print("*"*20)

t1="Python"
t2="123"
t3="Python 123"
t4="Python123"
t5="\t\n"
#13th method
print(t1.isalpha()) #here this function will check is ther only alphabets are present and give result in the form of true or falase
print(t2.isalpha())
print(t3.isalpha())
print("_"*20)

#14th method 
print(t1.isdigit())     #here this function will check is there only digits in string and give result in the form of true or falase
print(t2.isdigit())
print(t3.isdigit())
print("_"*20)

#15th method
print(t1.isalnum())     #here this function will check for only alphabets or digits, very imp statment
print(t2.isalnum())
print(t3.isalnum())
print(t4.isalnum())

print("_"*20)

#16th method
print(t1.isspace()) #for it is space is present
print(t2.isspace())
print(t3.isspace())
print(t4.isspace())
print(t5.isspace())     #isspace() method in Python returns True if a string contains only whitespace characters and is at least one character long. If the string contains any letters, numbers, symbols, or is entirely empty (""), it returns False












