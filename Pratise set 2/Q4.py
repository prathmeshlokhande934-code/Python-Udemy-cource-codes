#Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case


while True:
    day=int(input("Enter any number of day between 1 to 7: "))
    match day:
        case 1:
            print("Monday")
            print("Type any number greather than 7 to exit loop")
        case 2:
            print("Tuesday")
            print("Type any number greather than 7 to exit loop")
        case 3:
            print("Wednesday")
            print("Type any number greather than 7 to exit loop")
        case 4:
            print("Thursday")
            print("Type any number greather than 7 to exit loop")
        case 5:
            print("Friday")
            print("Type any number greather than 7 to exit loop")
        case 6:
            print("Saturday")
            print("Type any number greather than 7 to exit loop")
        case 7:
            print("Sunday")
            print("Type any number greather than 7 to exit loop")
        case _:
            break  #Type any number greather than 7 to exit loop