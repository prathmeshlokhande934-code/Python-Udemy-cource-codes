class Employee:
    def __init__(self,salary,name,age):
        self.salary=salary
        self.name=name
        self.age=age

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(self.name)
        print(self.age)

obj1=Employee(100000,"Prathmesh",20)
print(obj1.get_salary())
print(obj1.get_info())

obj2=Employee(50000,"Ram",21)
print(obj2.salary)
print(obj2.get_salary())
print(obj2.get_info())