#Use a while loop to reverse a given number (e.g., 123 → 321).

#1st approch 
    # num=int(input("Enter an number: "))
    # rev_num=0
    # while num!=0:
    #     digit=num%10
    #     rev_num=(rev_num*10)+digit
    #     num=num//10

    # print(rev_num)

# or anothier simple code is here
# 2nd approch

num=int(input("Enter any number")) 

# num1=str(num)
# num2=int(num1[::-1])
# print(num2)

# or another complex version is
#3rd approch

print(int(str(num)[::-1]))