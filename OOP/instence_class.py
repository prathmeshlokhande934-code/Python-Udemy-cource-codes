class employee:
    company="Asus" #this is the class instence
    def __init__(self,salary,name,bound,company):
        self.name=name
        self.salary=salary
        self.bound=bound
        self.company=company   #Here this company refers to instance of object which in this case is VIVO

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(self.name)
        print(self.bound)
        print(self.company)

ee=employee(1000,"Pram",2,"VIVO")
print(ee.get_salary())

ee.get_info()

print("Company of object mens instance of object:",ee.company)
print("Company of object mens instance of class is:",employee.company)  # type: ignore #this is writte but they give error

#object interosption
print(dir(ee))  #this gives all intances and methods that object can acces

#to ignore an warning we use "#type:ignore"  is used 