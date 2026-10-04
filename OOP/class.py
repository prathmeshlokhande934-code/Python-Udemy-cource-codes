class Bike:
    speed=150
    def run(self):      #Writting the self is mandatory insid the class for all methods.it refers to the object of the a class.
            print("Inside the class,Bike runs.")

b=Bike()    #object is created
b.run()     #FUN was called

b2=Bike()
b2.run()

print(b.speed)  #we can also acces the variables inside the class using object of that class
# print(speed) #this gives error