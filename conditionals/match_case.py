#match-case is an like an c++ switch case statement. It is used to match a value against a series of patternsand execute the corresponding block of code for the first matching pattern. 

num=int(input("Enter any number between  to 10: "))

match num:
    case 1:
        print("You win an computer.")
    
    case 4:
        print("you win an iphone.")

    case 9:
        print("You win an headphone.")

    case _:                             #this is an default case which will be executed if none of the above cases match.and it was written using _
        print("Better luck next time.")