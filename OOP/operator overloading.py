class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def sum(self,p):
        return point((self.x+p.x),(self.y+p.y))

    def point_print(self):
        print(f"X={self.x} and Y={self.y}")

    def __add__(self,p):        #this is operator overloading here we are overloading add operator to do addition of two objects parameters using "+" this operator
        return point((self.x+p.x),(self.y+p.y))       

p1=point(3,2)
p2=point(6,3)

# p=p1.sum(p2)

#insted of doing this we can use operator overloading
p=p1+p2
print(p.point_print())
